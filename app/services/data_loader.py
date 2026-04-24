from __future__ import annotations

from pathlib import Path

import pandas as pd


class DataLoaderError(Exception):
    """Raised when a dataset cannot be loaded."""


def load_csv(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        raise DataLoaderError(f"File not found: {file_path}")
    if path.suffix.lower() != ".csv":
        raise DataLoaderError("Only CSV files are supported in V1")

    try:
        return pd.read_csv(path)
    except Exception as exc:  # pragma: no cover
        raise DataLoaderError(f"Failed to read CSV: {exc}") from exc
