from __future__ import annotations

from typing import Any


def summarize_findings(profile: dict[str, Any], quality: dict[str, Any]) -> str:
    parts: list[str] = []
    parts.append(
        f"Dataset has {profile['row_count']} rows and {profile['column_count']} columns."
    )

    null_total = sum(quality["null_counts"].values()) if quality["null_counts"] else 0
    if null_total:
        parts.append(f"Detected {null_total} missing values across columns.")

    duplicates = quality["duplicate_row_count"]
    if duplicates:
        parts.append(f"Detected {duplicates} duplicate rows.")

    invalid_dates = sum(quality["invalid_dates"].values()) if quality["invalid_dates"] else 0
    if invalid_dates:
        parts.append(f"Detected {invalid_dates} invalid date values.")

    fmt_issues = len(quality["format_inconsistencies"])
    if fmt_issues:
        parts.append(f"Detected format inconsistencies in {fmt_issues} text columns.")

    if len(parts) == 1:
        parts.append("No major quality issues were found in this pass.")

    parts.append("Suggested next step: fix nulls/duplicates first, then re-run profiling.")
    return " ".join(parts)
