import logging
import os
import psycopg2

LOGGER: logging.Logger = logging.getLogger(__name__)

def connection_to_db() -> psycopg2.extensions.connection:
    try:
        conn: psycopg2.extensions.connection = psycopg2.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PWD"]
        )
        LOGGER.info("Connection to database established successfully")
        return conn
    except KeyError as error:
        LOGGER.error("Missing required environment variable: %s", error.args[0])
        raise
    except psycopg2.OperationalError:
        LOGGER.exception("Could not connect to database")
        raise
