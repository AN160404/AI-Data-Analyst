import os
import shutil
import tempfile
from fastapi import APIRouter, UploadFile, File, HTTPException
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient
from backend.services.data_loader import DataLoader
from backend.core.config import settings
from backend.core.dataset_registry import DatasetRegistry
from backend.core.duckdb_instance import duckdb_instance

router = APIRouter()
ALLOWED_EXTENSIONS = [".csv", ".xlsx"]


def get_blob_container():
    if not settings.AZURE_STORAGE_CONNECTION_STRING:
        raise RuntimeError("Azure Blob Storage connection string is not configured")

    blob_service_client = BlobServiceClient.from_connection_string(
        settings.AZURE_STORAGE_CONNECTION_STRING
    )
    container_name = settings.AZURE_STORAGE_CONTAINER_NAME or "uploads"
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
    except ResourceExistsError:
        pass
    return container_client


def upload_to_blob(container_client, local_path, blob_name):
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    return blob_client.url


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Handles file uploads, cleans the dataset, and registers it with the platform.
    """
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only CSV and XLSX files are allowed")

    if not settings.AZURE_STORAGE_CONNECTION_STRING:
        raise HTTPException(status_code=500, detail="Azure Blob Storage is not configured")

    temp_fd, temp_path = tempfile.mkstemp(suffix=file_extension)
    os.close(temp_fd)

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        df = DataLoader.load_dataset(temp_path)
        df, cleaning_report = DataLoader.clean_dataset(df)

        DatasetRegistry.register_dataset(file.filename, df)
        table_name = file.filename.split(".")[0].replace("-", "_").replace(" ", "_")
        duckdb_instance.register_dataframe(table_name, df)

        container_client = get_blob_container()
        blob_url = upload_to_blob(container_client, temp_path, os.path.basename(file.filename))

    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass
    
    return {
        "filename": file.filename,
        "blob_url": blob_url,
        "message": "File uploaded successfully",
        "cleaning_report": cleaning_report,
        "dataset_info": DataLoader.get_basic_info(df),
        "schema": DataLoader.get_schema(df),
        "preview": DataLoader.get_preview(df),
        "registered_datasets": DatasetRegistry.list_datasets(),
    }