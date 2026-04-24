from __future__ import annotations

import re
from collections import Counter
from typing import Iterable


def classify_string_pattern(value: str) -> str:
    """Return a simple shape label for a string value."""
    if value is None:
        return "empty"

    text = str(value).strip()
    if not text:
        return "empty"
    if re.fullmatch(r"\d+", text):
        return "numeric"
    if re.fullmatch(r"[A-Za-z]+", text):
        return "alpha"
    if re.fullmatch(r"[A-Za-z0-9]+", text):
        return "alnum"
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", text):
        return "email"
    if re.fullmatch(r"[\d\s\-\+\(\)]+", text):
        return "phone_like"
    return "mixed"


def dominant_pattern(values: Iterable[str]) -> tuple[str, float]:
    """Return dominant pattern and its ratio from input values."""
    labels = [classify_string_pattern(v) for v in values]
    labels = [label for label in labels if label != "empty"]
    if not labels:
        return "empty", 1.0

    counts = Counter(labels)
    top_label, top_count = counts.most_common(1)[0]
    ratio = top_count / len(labels)
    return top_label, ratio
