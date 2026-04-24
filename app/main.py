from __future__ import annotations

from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Azure AI Data Quality Copilot",
    description=(
        "Cloud-style assistant for dataset profiling, quality checks, and SQL generation"
    ),
    version="0.1.0",
)

app.include_router(router, prefix="/api/v1", tags=["copilot"])
