import csv
import sys

def normalize_row(row: dict[str, str]) -> dict[str, str]:
    return {k.strip(): v.strip() for k, v in row.items()}

def count_missing(rows: list[dict[str, str]], key: str) -> int:
    return sum(1 for r in rows if not r.get(key))

