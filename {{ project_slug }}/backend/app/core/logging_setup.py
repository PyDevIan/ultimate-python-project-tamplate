from __future__ import annotations
import os
import logging
from pathlib import Path
from loguru import logger
import sys

class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except Exception:
            level = record.levelno
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_dir = Path(os.getenv("LOG_DIR", "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / os.getenv("LOG_FILE", "app.log")

    logger.remove()
    logger.add(
        sink=sys.stderr,
        level=log_level,
        colorize=True,
        format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | {message}",
    )
    logger.add(
        log_file,
        rotation="10 MB",
        retention="14 days",
        compression="zip",
        enqueue=True,
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    )

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    return logger
