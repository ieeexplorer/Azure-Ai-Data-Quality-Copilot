from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    AskRequest,
    AskResponse,
    FileRequest,
    ProfileResponse,
    QualityResponse,
    SqlRequest,
    SqlResponse,
)
from app.services.ai_assistant import summarize_findings
from app.services.data_loader import DataLoaderError, load_csv
from app.services.profiler import profile_dataframe
from app.services.quality_checks import run_quality_checks
from app.services.sql_generator import generate_sql

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/profile", response_model=ProfileResponse)
def profile_data(request: FileRequest) -> ProfileResponse:
    try:
        df = load_csv(request.file_path)
    except DataLoaderError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return ProfileResponse(profile=profile_dataframe(df))


@router.post("/quality-checks", response_model=QualityResponse)
def quality_checks(request: FileRequest) -> QualityResponse:
    try:
        df = load_csv(request.file_path)
    except DataLoaderError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return QualityResponse(quality_checks=run_quality_checks(df))


@router.post("/generate-sql", response_model=SqlResponse)
def generate_sql_query(request: SqlRequest) -> SqlResponse:
    return SqlResponse(sql=generate_sql(request.question, request.table_name))


@router.post("/ask", response_model=AskResponse)
def ask_data_assistant(request: AskRequest) -> AskResponse:
    question_lower = request.question.strip().lower()

    if "sql" in question_lower or "query" in question_lower:
        sql = generate_sql(request.question)
        return AskResponse(answer="Generated SQL from your request.", sql=sql)

    try:
        df = load_csv(request.file_path)
    except DataLoaderError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    profile = profile_dataframe(df)
    quality = run_quality_checks(df)
    summary = summarize_findings(profile, quality)
    return AskResponse(answer=summary, profile=profile, quality_checks=quality)
