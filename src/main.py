from dotenv import load_dotenv
import json
import logging

from .config import to_config_root_logger
from .services import fetch_employee, EmployeeData
from .utils import parse_to_json

DOTENV_LOADED: bool = load_dotenv()

to_config_root_logger()

LOGGER: logging.Logger = logging.getLogger(__name__)

def main() -> None:
    if DOTENV_LOADED:
        LOGGER.info(".env file loaded successfully")
    else:
        LOGGER.warning(".env file failed to load")

    employee_data: EmployeeData = fetch_employee()
    
    parse_to_json(employee_data)

if __name__ == "__main__":
    main()
    