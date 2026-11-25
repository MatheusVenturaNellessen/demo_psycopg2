import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def to_config_root_logger() -> None:    
    logs_path: Path = Path("logs/app.log")
    logs_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    
    logging.basicConfig(
        force=True, # not ideal
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(filename)s:%(funcName)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            RotatingFileHandler(
                filename=logs_path,
                maxBytes=5*1024*1024,
                backupCount=3,
                encoding="utf-8",
                delay=True
            ),
            logging.StreamHandler(sys.stdout)
        ]
    )
