from datetime import datetime
import logging
import psycopg2

from ..db import connection_to_db

LOGGER: logging.Logger = logging.getLogger(__name__)

EmployeeData = list[tuple[int, str, str, datetime]]

def fetch_employee() -> EmployeeData:
    conn: psycopg2.extensions.connection | None = None
    try:
        conn = connection_to_db()
        with conn:
            with conn.cursor() as cursor:
                query: str = "SELECT emp_id, emp_name, emp_email, created_at FROM employees"
                cursor.execute(query)
                rows: EmployeeData = cursor.fetchall()
                for row in rows:
                    emp_id, emp_name, emp_email, created_at = row
                    LOGGER.info(
                        "Employee ID: %s | Employee name: %s | Employee e-mail: %s | Create at: %s",
                        emp_id,
                        emp_name,
                        emp_email,
                        created_at
                    )
                return rows
    except psycopg2.DatabaseError:
        LOGGER.exception("Error while quering in database")
        raise
    finally:
        if conn is not None:
            conn.close()
            LOGGER.info("Connection to databse closed successfully")
