from __future__ import annotations

from typing import Any

import pandas as pd


def profile_dataframe(df: pd.DataFrame) -> dict[str, Any]:
    columns: list[dict[str, Any]] = []

    for column in df.columns:
        series = df[column]
        columns.append(
            {
                "name": column,
                "dtype": str(series.dtype),
                "non_null_count": int(series.notna().sum()),
                "null_count": int(series.isna().sum()),
                "unique_count": int(series.nunique(dropna=True)),
                "sample_values": [
                    None if pd.isna(v) else str(v)
                    for v in series.drop_duplicates().head(5).tolist()
                ],
            }
        )

    return {
        "row_count": int(df.shape[0]),
        "column_count": int(df.shape[1]),
        "memory_usage_bytes": int(df.memory_usage(deep=True).sum()),
        "columns": columns,
    }
