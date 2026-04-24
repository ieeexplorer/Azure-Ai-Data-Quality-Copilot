from __future__ import annotations

from typing import Any

import pandas as pd

from app.utils.helpers import dominant_pattern


def _check_invalid_dates(df: pd.DataFrame) -> dict[str, int]:
    invalid_dates: dict[str, int] = {}

    for column in df.columns:
        if "date" not in str(column).lower():
            continue

        series = df[column]
        non_null = series.dropna().astype(str)
        if non_null.empty:
            continue

        parsed = pd.to_datetime(non_null, errors="coerce")
        invalid_count = int(parsed.isna().sum())
        if invalid_count > 0:
            invalid_dates[column] = invalid_count

    return invalid_dates


def _check_format_inconsistency(df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    inconsistencies: dict[str, dict[str, Any]] = {}

    object_columns = df.select_dtypes(include=["object", "str"]).columns
    for column in object_columns:
        values = df[column].dropna().astype(str)
        if len(values) < 3:
            continue

        top_pattern, ratio = dominant_pattern(values)
        if ratio < 0.8:
            inconsistencies[column] = {
                "dominant_pattern": top_pattern,
                "consistency_ratio": round(ratio, 2),
            }

    return inconsistencies


def run_quality_checks(df: pd.DataFrame) -> dict[str, Any]:
    null_counts = {
        column: int(df[column].isna().sum())
        for column in df.columns
        if int(df[column].isna().sum()) > 0
    }

    duplicate_row_count = int(df.duplicated().sum())
    invalid_dates = _check_invalid_dates(df)
    format_inconsistencies = _check_format_inconsistency(df)

    issue_count = (
        sum(null_counts.values())
        + duplicate_row_count
        + sum(invalid_dates.values())
        + len(format_inconsistencies)
    )

    return {
        "null_counts": null_counts,
        "duplicate_row_count": duplicate_row_count,
        "invalid_dates": invalid_dates,
        "format_inconsistencies": format_inconsistencies,
        "total_issue_score": int(issue_count),
    }
