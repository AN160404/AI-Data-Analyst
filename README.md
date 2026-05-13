# AI Data Analyst Agent

An AI-powered Business Intelligence and Analytics Platform built using FastAPI, LangGraph, OpenRouter LLMs, DuckDB, Prophet, and Multi-Agent AI Workflows.

The platform allows users to upload CSV/Excel datasets, ask analytical questions in natural language, generate charts dynamically, obtain AI-driven business insights, and perform autonomous data analysis and time-series forecasting using specialized AI agents.

---

# Features

## Dataset Management
- Upload CSV and Excel datasets
- Automatic dataset registration
- Dataset preview and schema extraction
- Dataset cleaning and preprocessing

---

## AI-Powered Analytics
- Natural language analytical queries
- AI-generated SQL queries
- DuckDB-powered analytical execution
- Business insight generation
- KPI extraction and grounded analytics

---

## AI Forecasting & Predictive Analytics
- **Time-Series Forecasting**: Automated forecasting using Facebook Prophet.
- **Trend Detection**: AI-driven analysis of upward, downward, and stable trends.
- **Predictive Insights**: Natural-language business insights derived from forecast models.
- **Confidence Intervals**: Visual representation of prediction uncertainty (95% CI).
- **Automated Chart Config**: Frontend-ready JSON configurations for forecast visualizations.

---

## Dynamic Visualization
- AI-generated chart configurations
- Automatic chart type selection
- Frontend-ready visualization JSON

Supported chart types:
- Bar charts
- Line charts
- Pie charts
- Scatter plots
- **Forecast charts** (with confidence intervals)

---

## Multi-Agent Architecture
- **Supervisor Agent**: Intelligently routes user requests based on intent classification.
- **SQL Analysis Agent**: Generates and executes analytical SQL queries.
- **Forecast Agent**: Orchestrates time-series predictions and trend analysis.
- **Insight Generation Agent**: Produces descriptive business insights from data.
- **Visualization Agent**: Determines the best visual representation for results.

---

# Tech Stack

## Backend
- FastAPI
- Python
- DuckDB
- Pandas
- **Prophet** (Time-Series Forecasting)
- LangChain / LangGraph
- OpenRouter API

---

## AI & Analytics
- OpenRouter LLMs (GPT-4o / Claude 3.5 Sonnet)
- Multi-Agent AI Architecture
- Workflow Orchestration
- KPI Grounding
- AI-driven SQL & Insight Generation

---

# AI Forecasting & Predictive Analytics

The platform features a specialized forecasting subsystem designed to provide stakeholders with future-looking metrics.

### Forecasting Architecture
The forecasting system operates as a specialized agent-led workflow:
1. **Intent Classification**: The Supervisor Agent detects forecasting intent (keywords: *forecast, predict, future, projection*).
2. **Validation**: The system ensures the dataset contains valid date and numeric columns.
3. **Modeling**: The Forecast Service utilizes **Facebook Prophet** for robust time-series modeling, handling seasonality and outliers automatically.
4. **Insight Generation**: The Forecast Insight Service analyzes the model's slope and generates a natural-language business narrative.
5. **Visualization**: The Forecast Chart Service produces a JSON configuration including predictions and confidence intervals for frontend rendering.

### Capabilities
- **Revenue & Sales Prediction**: Predict future financial performance based on historical data.
- **Confidence Interval Analysis**: Understand the upper and lower bounds of predictions.
- **Automated Trend Detection**: Immediate identification of growth, decline, or stability.

### API Request Example
```http
POST /agent
Content-Type: application/json

{
    "dataset_name": "sales_data.csv",
    "question": "Predict our revenue for the next 30 days",
    "date_column": "order_date",
    "target_column": "revenue"
}
```

### API Response Example
```json
{
    "task_type": "forecasting",
    "result": {
        "status": "success",
        "agent": "Forecast Agent",
        "dataset": "sales_data.csv",
        "target_column": "revenue",
        "insight": "Revenue is expected to increase over the next 30 days based on a strong upward trend.",
        "forecast": [...],
        "chart_config": {
            "type": "forecast_chart",
            "datasets": [
                { "label": "Predicted Value", "data": [105.2, 108.4, ...] },
                { "label": "Confidence Interval", "data": [{"low": 98.1, "high": 112.3}, ...] }
            ]
        }
    }
}
```

---

# Project Architecture

```text
User
 ↓
Frontend Dashboard
 ↓
FastAPI APIs
 ↓
Supervisor Agent
 ↓
Specialized Agents (SQL, Forecast, Insight, Viz)
 ↓
LangGraph Workflows
 ↓
Services (Prophet, DuckDB, LLM)
 ↓
Datasets
```

---

# Folder Structure

```text
backend/
├── agents/
│   ├── supervisor_agent.py
│   ├── sql_agent.py
│   ├── forecast_agent.py          # NEW: Orchestrates forecasting tasks
│   ├── insight_agent.py
│   └── visualization_agent.py
│
├── api/
│   └── agent.py                   # Main entry point for AI agents
│
├── services/
│   ├── forecast_service.py        # NEW: Prophet model execution
│   ├── forecast_validator.py      # NEW: Input validation for forecasting
│   ├── forecast_insight_service.py # NEW: Trend & NL insight generation
│   ├── forecast_chart_service.py   # NEW: Frontend-ready chart configs
│   ├── llm_service.py
│   ├── visualization_service.py
│   └── insight_service.py
│
├── main.py
```

---

# Frontend Documentation

## Overview
The frontend is a **Streamlit-based dashboard** that provides an intuitive interface for interacting with the AI Data Analyst platform. It enables users to upload datasets, generate insights, build workflows, and collaborate with the AI agent seamlessly.

### Tech Stack
- **Streamlit** — Modern web framework for rapid UI development
- **Python** — Backend logic and API integration
- **Custom CSS/Theme** — Dark theme with professional styling
- **REST API Integration** — Communicates with FastAPI backend

---

## Frontend Architecture

```text
Frontend Dashboard (Streamlit)
    ├── Home Page (Landing)
    ├── Pages
    │   ├── 1_Dataset_Onboarding.py      — Upload & register datasets
    │   ├── 2_Registered_Datasets.py     — View registered datasets & metadata
    │   ├── 3_Insights_Suite.py          — Generate business insights
    │   ├── 4_Workflow_Intelligence.py   — Inspect SQL pipeline & data flow
    │   └── 5_AI_Analyst.py              — Chat with AI agent & visualize results
    │
    └── Utilities (utils/)
        ├── api_client.py      — API request handlers
        ├── theme.py           — Dark theme styling & CSS
        ├── present.py         — Result formatting & display components
        ├── charts.py          — Chart rendering (Altair/Plotly)
        ├── config.py          — Configuration management
        └── __init__.py
```

---

## Pages & Features

### 1. **Home Page** (`Home.py`)
**Landing page with platform overview and quick navigation.**

**Features:**
- Enterprise analytics experience header
- Backend health status indicator (API connectivity check)
- Feature showcase (4-column grid with icons)
- Quick navigation links to all sections

**Key Sections:**
- Status card showing API connection state
- Feature cards highlighting core capabilities
- Navigation guide for users

---

### 2. **Dataset Onboarding** (`pages/1_Dataset_Onboarding.py`)
**Upload and register CSV/XLSX datasets for analysis.**

**Features:**
- Drag-and-drop file uploader (CSV/XLSX)
- One-click upload & registration workflow
- Dataset preview (schema, sample rows, cleaning summary)
- Automatic dataset registration in the system
- Upload history tracking

**Workflow:**
1. User selects a CSV or XLSX file
2. Clicks "Upload & register" button
3. Backend processes and validates the file
4. Dataset is registered and displayed with metadata
5. User can proceed to analytics or upload another file

**API Endpoint:** `POST /upload`

---

### 3. **Registered Datasets** (`pages/2_Registered_Datasets.py`)
**Browse and explore all registered datasets and their metadata.**

**Features:**
- List all registered datasets
- View dataset metadata (name, columns, row count, file size)
- Dataset preview and schema inspection
- Filter and search functionality

**Use Cases:**
- Verify registered datasets before analysis
- Check data shape and types
- Confirm dataset availability for insights/forecasting

**API Endpoint:** `GET /datasets`

---

### 4. **Insights Suite** (`pages/3_Insights_Suite.py`)
**Generate AI-driven business insights and KPI dashboards.**

**Features:**
- Dataset selection dropdown
- One-click insight generation
- Automated KPI extraction
- Narrative-based business insights
- Formatted results display

**Generated Insights Include:**
- Summary statistics
- KPI dashboards
- Business narratives
- Trend observations
- Actionable recommendations

**Workflow:**
1. User selects a registered dataset
2. Clicks "Run" to generate insights
3. Backend analyzes data and extracts KPIs
4. Formatted insights display with charts

**API Endpoint:** `GET /generate-insights`

---

### 5. **Workflow Intelligence** (`pages/4_Workflow_Intelligence.py`)
**Inspect SQL pipeline transformations and data flow.**

**Features:**
- Visualize data transformation pipeline
- SQL query inspection
- Dependency chain visualization
- Workflow state inspection
- Execution history tracking

**Use Cases:**
- Audit data transformations
- Debug SQL queries
- Understand data lineage
- Validate workflow integrity

**API Endpoint:** `GET /workflow`

---

### 6. **AI Analyst** (`pages/5_AI_Analyst.py`)
**Interactive chat interface with multi-agent AI assistant.**

**Features:**
- Natural language query input
- Dataset selection
- Optional forecasting parameters (date column, target column)
- Multi-task agent routing (SQL queries, insights, forecasting)
- Dynamic chart generation
- Real-time result display
- Conversational analytics

**Supported Query Types:**
- **SQL Analytics**: "Show total sales by category"
- **Forecasting**: "Predict revenue for the next 30 days"
- **Insights**: "Summarize key trends in this data"
- **Visualization**: "Create a scatter plot of X vs Y"

**Forecasting Options:**
- Optional manual column selection
- Auto-detection if not specified
- Confidence interval visualization
- Trend analysis

**Workflow:**
1. User selects a dataset
2. Enters a natural language question
3. (Optional) Specifies date and target columns for forecasting
4. Clicks "Ask agent"
5. Backend routes to appropriate agent (SQL, Forecast, Insight, Viz)
6. Results display with charts/insights

**API Endpoint:** `POST /agent`

---

## Frontend Utilities

### `api_client.py`
Handles all API communication with the backend.

**Key Functions:**
- `health()` — Check API connectivity
- `upload_file()` — Upload datasets to backend
- `list_datasets()` — Retrieve registered datasets
- `generate_insights()` — Generate business insights
- `run_agent()` — Send queries to AI agent
- `get_workflow()` — Fetch workflow details

---

### `theme.py`
Custom dark theme styling for professional appearance.

**Features:**
- Brand color palette (primary, secondary, accent colors)
- Dark gradient background
- Responsive typography
- Card and component styling
- Hover effects and transitions
- **Mesh grid background** (subtle white grid overlay)

**Color Variables:**
- `--brand-bg`: #081423 (main background)
- `--brand-primary`: #01b8aa (teal/cyan)
- `--brand-secondary`: #f2c80f (yellow)
- `--brand-accent`: #f48c06 (orange)

---

### `present.py`
Format and display API responses in user-friendly layouts.

**Key Functions:**
- `display_upload_response()` — Show dataset upload results
- `display_insights_response()` — Display insights with charts
- `display_agent_response()` — Show AI agent results
- Custom formatting for KPIs, charts, and narratives

---

### `charts.py`
Chart rendering using Altair and Plotly.

**Supported Chart Types:**
- Bar charts
- Line charts
- Scatter plots
- Pie charts
- Forecast charts (with confidence intervals)

---

### `config.py`
Configuration management (API base URL, environment settings).

**Key Functions:**
- `get_api_base()` — Retrieve API base URL
- Environment variable handling
- Default configuration fallbacks

---

## Running the Frontend

### Prerequisites
- Python 3.8+
- Streamlit
- Backend running at the specified API_BASE_URL

### Setup

1. **Install dependencies**:
   ```bash
   cd frontend
   pip install -r requirements.txt
   ```

2. **Set environment variables** (optional):
   ```bash
   export API_BASE_URL=http://localhost:8000
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run Home.py
   ```

4. **Access the dashboard**:
   Open your browser to `http://localhost:8501`

### Configuration
The frontend looks for the backend API at:
- Environment variable: `API_BASE_URL` (default: `http://localhost:8000`)
- Fallback: Displayed in the UI for user awareness

---

## Styling & Customization

### Theme System
All styling is managed through `utils/theme.py`. The CSS includes:
- CSS variables for brand colors
- Responsive layouts
- Dark theme with accent colors
- Hover and transition effects
- **Mesh grid background** for visual depth

### Customizing the Theme
Edit `utils/theme.py` to modify:
- Brand colors (CSS variables)
- Background gradients
- Font sizes and spacing
- Card and button styling
- Mesh grid opacity/spacing

---

## API Integration

The frontend communicates with the backend via REST endpoints. All requests are handled through `utils/api_client.py`:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Check backend status |
| `/upload` | POST | Upload and register datasets |
| `/datasets` | GET | List registered datasets |
| `/generate-insights` | GET | Generate business insights |
| `/agent` | POST | Query multi-agent AI system |
| `/workflow` | GET | Inspect data pipeline |

---

## User Workflow

```
1. Home Page (Landing)
   ↓
2. Dataset Onboarding (Upload CSV/XLSX)
   ↓
3. Registered Datasets (Verify upload)
   ↓
4. Insights Suite / AI Analyst / Workflow Intelligence
   ├─ Generate insights automatically
   ├─ Ask natural language questions
   └─ Inspect transformation pipeline
   ↓
5. Results & Visualization
   ├─ Charts and KPIs
   ├─ Narrative insights
   └─ Forecast predictions
```

---

# Installation & Setup

## Backend Setup

1. **Clone & Install**:
   ```bash
   git clone <repo-url>
   cd AI-Data-Analyst
   pip install -r requirements.txt
   ```

2. **Environment Setup**:
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   API_BASE_URL=http://localhost:8000
   ```

3. **Run Backend Server**:
   ```bash
   uvicorn backend.main:app --reload
   ```
   Backend will be available at `http://localhost:8000`

## Frontend Setup

1. **Install Dependencies**:
   ```bash
   cd frontend
   pip install -r requirements.txt
   ```

2. **Set API Configuration** (optional):
   ```bash
   export API_BASE_URL=http://localhost:8000
   ```

3. **Run Frontend**:
   ```bash
   streamlit run Home.py
   ```
   Dashboard will open at `http://localhost:8501`

## Verification

- Backend Health: Navigate to `http://localhost:8000/health`
- Frontend Status Card: Shows API connection status on home page
- Upload Test: Try uploading a sample CSV file to verify end-to-end workflow

---

# Current Completed Features
* Dataset Upload & Registry
* Multi-Agent Intent Routing
* AI-Generated SQL Analytics (DuckDB)
* **AI Forecasting & Predictive Analytics (Prophet)**
* **Natural-Language Forecast Insights**
* **Dynamic Forecast Chart Configurations**
* LangGraph Workflow Orchestration
* Business Insight Generation

---

# Team Responsibilities

### Atia Naim
* AI Backend Architecture & Multi-Agent System
* LangGraph Workflow Orchestration

### Sriya Pandey
* **Forecasting & Predictive Analytics**
* Prophet Integration & Statistical Intelligence
* Trend Analysis & Insight Logic

### Amaan Shahid
* Frontend Dashboard & UI/UX Development
* API Integration & Deployment

---

# License
MIT License
