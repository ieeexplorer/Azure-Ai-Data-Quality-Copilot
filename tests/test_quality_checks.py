from __future__ import annotations

from pathlib import Path

from app.services.data_loader import load_csv
from app.services.quality_checks import run_quality_checks


def test_quality_checks_detects_known_issues() -> None:
    data_path = Path(__file__).resolve().parents[1] / "data" / "sample_customers.csv"
    df = load_csv(str(data_path))

    result = run_quality_checks(df)

    assert result["duplicate_row_count"] >= 1
    assert "email" in result["null_counts"]
    assert "signup_date" in result["invalid_dates"]
