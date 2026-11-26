from dotenv import load_dotenv

from .config import to_config_root_logger
from .services import fetch_employee, EmployeeData
from .utils import parse_to_json

load_dotenv()
to_config_root_logger()

def main() -> None:
    employee_data: EmployeeData = fetch_employee()
    parse_to_json(employee_data)

if __name__ == "__main__":
    main()
