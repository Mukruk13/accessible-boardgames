# logic/commands/save_config.py

import logging
from typing import Dict, Any
from utils.config import save_config as _save_config

logger = logging.getLogger(__name__)

def save_config(data: Dict[str, Any]) -> None:
    """
    Save configuration data by updating the config file.

    Args:
        data (Dict[str, Any]): Dictionary containing configuration keys and values to save.
    """
    logger.info(f"Saving config data: {data}")
    try:
        _save_config(data)
        logger.info("Configuration saved successfully.")
    except Exception as e:
        logger.error(f"Error saving configuration: {e}")
