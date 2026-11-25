import json
import logging
from pathlib import Path

from .serialize_data import serialize_data
from ..services import EmployeeData

LOGGER: logging.Logger = logging.getLogger(__name__)

def parse_to_json(employee_data: EmployeeData) -> None:
    json_path: Path = Path("employeeData.json")
    json_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    try:
        with open(
            file=json_path,
            mode="w",
            encoding="utf-8"
        ) as file:
            json.dump(
                obj=employee_data,
                fp=file,
                default=serialize_data,
                ensure_ascii=False,
                indent=2
            )
            LOGGER.info("%s created successfully", json_path)
    except json.JSONDecodeError:
        LOGGER.exception("Failed to serialize employee data to JSON file")
