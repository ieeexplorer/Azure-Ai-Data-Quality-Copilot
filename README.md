# Azure-AI-Data-Quality-Copilot

Cloud-style AI assistant for data profiling, quality checks, SQL generation, and natural-language data exploration, designed around Azure architecture patterns.

## Why this project

- Aligns with Azure data and AI engineering roles
- Demonstrates practical system design over isolated notebooks
- Combines Python, APIs, data quality engineering, and AI-assisted workflows

## Core features

- Load a CSV dataset from local path (V1)
- Profile dataset structure and column-level characteristics
- Detect nulls, duplicates, invalid date values, and format inconsistencies
- Ask plain-English data questions
- Generate SQL templates from natural-language prompts
- Return human-readable summaries and next-step recommendations

## Architecture mapping (conceptual)

| Project part | Azure mapping |
|---|---|
| File storage | Azure Blob Storage / Data Lake |
| Data ingestion | Azure Data Factory |
| Processing | Azure Databricks / Python backend |
| Database | Azure SQL Database |
| AI assistant | Azure OpenAI |
| Search | Azure AI Search |
| API hosting | Azure Functions / Azure App Service |
| Monitoring | Azure Monitor |

## Project structure

```text
Azure-AI-Data-Quality-Copilot/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── data_loader.py
│   │   ├── profiler.py
│   │   ├── quality_checks.py
│   │   ├── sql_generator.py
│   │   └── ai_assistant.py
│   ├── models/
│   │   └── schemas.py
│   └── utils/
│       └── helpers.py
├── data/
│   └── sample_customers.csv
├── tests/
│   ├── test_profiler.py
│   └── test_quality_checks.py
├── notebooks/
│   └── exploration.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Quickstart

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API:

```bash
uvicorn app.main:app --reload
```

4. Open docs:

```text
http://127.0.0.1:8000/docs
```

## API endpoints

- `GET /api/v1/health`
- `POST /api/v1/profile`
- `POST /api/v1/quality-checks`
- `POST /api/v1/generate-sql`
- `POST /api/v1/ask`

### Example request: profile

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/profile" \
  -H "Content-Type: application/json" \
  -d "{\"file_path\": \"data/sample_customers.csv\"}"
```

### Example request: SQL generation

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/generate-sql" \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Give me SQL to count churn by country\", \"table_name\": \"customers\"}"
```

## Testing

```bash
pytest -q
```

## Resume bullet

Built an Azure-style AI data quality copilot that profiles datasets, detects nulls and duplicates, generates SQL queries from plain English, and suggests corrective actions using Python, FastAPI, pandas, and cloud-oriented architecture patterns.

## Roadmap

- Azure Blob Storage integration for cloud file handling
- Azure SQL database integration
- Authentication and authorization
- Frontend dashboard
- Azure OpenAI for richer summarization and recommendations
- Azure AI Search for schema and data dictionary discovery
- Containerized deployment with Azure Container Apps
