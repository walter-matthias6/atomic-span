import csv
import sys

def normalize_row(row: dict[str, str]) -> dict[str, str]:
    return {k.strip(): v.strip() for k, v in row.items()}
