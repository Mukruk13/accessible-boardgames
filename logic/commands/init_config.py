# logic/commands/init_config.py

import logging

from utils.config_manager import ConfigManager

logger = logging.getLogger(__name__)


def initialize_config() -> None:
    """
    Ensure the configuration file exists at application startup.

    If the config file is missing, it will be created with default values.
    """
    logger.info("Initializing configuration file...")
    try:
        # Ensures file exists via ConfigManager initialization
        ConfigManager.get_instance()
        logger.info("Configuration file exists or was created successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize configuration file: {e}")
