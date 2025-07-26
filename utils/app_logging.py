# utils/app_logging.py

import logging
import os
from typing import Optional


def setup_logging(log_to_file: Optional[bool] = False) -> None:
    """
    Configures logging for the application.

    - Adds a StreamHandler (console output) at INFO level if not already present.
    - Optionally adds a FileHandler writing to 'dev_tools/app.log' at DEBUG level.
    - Sets the root logger level to DEBUG to capture all logs.
    - Ensures no duplicate handlers are added on repeated calls.

    Args:
        log_to_file (bool, optional): Whether to log to a file as well. Defaults to False.
    """
    log_format = "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
    formatter = logging.Formatter(log_format)

    root_logger = logging.getLogger()  # Kivy uses root logger

    if not any(isinstance(handler, logging.StreamHandler) for handler in root_logger.handlers):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    if log_to_file:
        log_file_path = os.path.abspath("dev_tools/app.log")
        print(f"Logging to file: {log_file_path}")

        if not any(
            isinstance(handler, logging.FileHandler) and getattr(handler, "baseFilename", None) == log_file_path
            for handler in root_logger.handlers
        ):
            file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)

    root_logger.setLevel(logging.DEBUG)



