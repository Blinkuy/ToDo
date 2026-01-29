import logging
import logging.config
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def setup_root_logger(level: int = logging.INFO) -> None:
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": LOG_DIR / "app.log",
                "maxBytes": 10 * 1024 * 1024,
                "backupCount": 5,
                "formatter": "standard",
                "encoding": "utf-8",
                "level": level,
            },
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "level": level,
            },
        },
        "root": {
            "handlers": ["file", "console"],
            "level": level,
        },
        "loggers": {
            "uvicorn": {"level": "INFO"},
            "uvicorn.access": {"level": "WARNING"},
            "aiokafka": {"level": "WARNING"},
        },
    }

    logging.config.dictConfig(logging_config)
