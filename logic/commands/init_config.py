# logic/commands/init_config.py

import logging
from utils.config import ensure_config_exists

logger = logging.getLogger(__name__)

def initialize_config() -> None:
    """
    Ensure the configuration file exists at application startup.
    Creates default config if missing.
    """
    logger.info("Initializing configuration file...")
    try:
        ensure_config_exists()
        logger.info("Configuration file exists or was created successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize configuration file: {e}")
