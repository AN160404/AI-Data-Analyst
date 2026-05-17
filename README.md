# AI Data Analyst Agent

A polished analytics platform that combines Streamlit, FastAPI, DuckDB, AI agents, and Azure Blob Storage to provide fast dataset onboarding, natural-language analytics, forecasting, and workflow inspection.

## What It Does
- Upload CSV/XLSX datasets for automated cleaning and registration
- Generate business insights from registered data
- Answer natural language analytics questions via a multi-agent AI assistant
- Produce time-series forecasts with confidence intervals
- Inspect workflow and SQL pipeline behavior
- Persist uploaded files to Azure Blob Storage

## Core Features

| Category | Capabilities |
| --- | --- |
| Dataset Management | Upload, clean, preview, and register CSV/XLSX files |
| AI Analytics | Natural language queries, SQL generation, KPI extraction |
| Forecasting | Prophet-based time-series prediction, trend detection, confidence intervals |
| Visualization | Chart-ready output, bar/line/pie/scatter/forecast charts |
| Workflow | Agent routing, pipeline inspection, query debugging |
| Storage | Azure Blob Storage for upload persistence |

## Architecture

### Backend
- FastAPI API server
- DuckDB for analytics and dataset registration
- AI agents for SQL, insight, forecast, and visualization tasks
- Azure Blob Storage integration for upload persistence

### Frontend
- Streamlit dashboard with a unified dark theme
- Navigation pages for dataset onboarding, insights, AI chat, and workflow intelligence
- REST API client layer in `frontend/utils/api_client.py`

## Azure Blob Storage

Uploaded files are now stored in Azure Blob Storage as part of the backend upload flow.

### How it works
1. Client uploads a file to `POST /upload`
2. Backend writes the file to a temporary local path
3. Dataset is loaded, cleaned, and registered
4. File is uploaded to Azure Blob Storage
5. Local temporary file is deleted
6. Response returns metadata and `blob_url`

### Required environment variables
```env
AZURE_STORAGE_CONNECTION_STRING=<connection-string>
AZURE_STORAGE_CONTAINER_NAME=uploads
```

### Benefits
- Removes long-term reliance on local disk
- Supports production-grade deployment
- Keeps uploaded datasets accessible and durable

## Pages

| Page | Purpose |
| --- | --- |
| `Home.py` | Dashboard landing page and status overview |
| `pages/1_Dataset_Onboarding.py` | Upload and register datasets |
| `pages/2_Registered_Datasets.py` | List registered datasets |
| `pages/3_Insights_Suite.py` | Generate business insights |
| `pages/4_Workflow_Intelligence.py` | Inspect workflows and SQL pipelines |
| `pages/5_AI_Analyst.py` | Ask questions and get charts/forecasts |

## API Endpoints

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/health` | GET | Check backend status |
| `/upload` | POST | Upload and register datasets |
| `/datasets` | GET | List registered datasets |
| `/generate-insights` | GET | Generate business insights |
| `/agent` | POST | Query multi-agent AI system |
| `/workflow` | GET | Inspect workflow state |

## Setup

### Backend
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` with at least:
```env
DATABASE_URL=sqlite:///./app.db
AZURE_STORAGE_CONNECTION_STRING=<connection-string>
AZURE_STORAGE_CONTAINER_NAME=uploads
MODEL_NAME=gpt-4o
```

Run the backend:
```bash
uvicorn backend.main:app --reload
```

### Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run Home.py
```

Open `http://localhost:8501`

## Notes
- The backend uses DuckDB and Prophet for analytics and forecasting.
- Azure Blob Storage is enabled for dataset upload persistence.
- The frontend uses a shared theme in `frontend/utils/theme.py`.
- The multi-agent system routes queries to specialized agents for SQL, insights, forecasting, and visualization.
