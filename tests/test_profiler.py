from __future__ import annotations

from pathlib import Path

from app.services.data_loader import load_csv
from app.services.profiler import profile_dataframe


def test_profile_dataframe_has_expected_keys() -> None:
    data_path = Path(__file__).resolve().parents[1] / "data" / "sample_customers.csv"
    df = load_csv(str(data_path))

    result = profile_dataframe(df)

    assert "row_count" in result
    assert "column_count" in result
    assert "columns" in result
    assert result["row_count"] > 0
    assert result["column_count"] == len(result["columns"])
