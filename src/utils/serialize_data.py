from datetime import datetime
import logging

LOGGER: logging.Logger = logging.getLogger(__name__)

# Type later...
def serialize_data(obj):
    if not isinstance(obj, (datetime,)):
        LOGGER.error("Object given is not serializable")
        raise TypeError(f"Object given ({type(obj)}) is not serializable")
    return obj.isoformat()
