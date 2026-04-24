from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class FileRequest(BaseModel):
    file_path: str = Field(..., description="Path to a CSV file")


class SqlRequest(BaseModel):
    question: str = Field(..., min_length=3)
    table_name: str = Field(default="customers", min_length=1)


class AskRequest(BaseModel):
    file_path: str = Field(..., description="Path to a CSV file")
    question: str = Field(..., min_length=3)


class ProfileResponse(BaseModel):
    profile: dict[str, Any]


class QualityResponse(BaseModel):
    quality_checks: dict[str, Any]


class SqlResponse(BaseModel):
    sql: str


class AskResponse(BaseModel):
    answer: str
    sql: str | None = None
    profile: dict[str, Any] | None = None
    quality_checks: dict[str, Any] | None = None
