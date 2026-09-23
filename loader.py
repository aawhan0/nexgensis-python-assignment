"""Input loading helpers for the delivery simulation."""

import json
from pathlib import Path
from typing import Any


def load_data(path: str | Path) -> dict[str, Any]:
    """Load the assignment input JSON and return it as a dictionary."""
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Input JSON must contain an object at the top level.")

    required_sections = {"warehouses", "agents", "packages"}
    missing_sections = required_sections - data.keys()

    if missing_sections:
        missing = ", ".join(sorted(missing_sections))
        raise ValueError(f"Input JSON is missing required sections: {missing}")

    return data
