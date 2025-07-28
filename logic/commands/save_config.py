# logic/commands/save_config.py

from utils.config_manager import ConfigManager
import logging

logger = logging.getLogger(__name__)

def save_config(new_data: dict):
    logger.info(f"Saving config data: {new_data}")
    try:
        config = ConfigManager.get_instance()
        for key, value in new_data.items():
            config.set(key, value)
        logger.debug("Configuration saved successfully.")
    except Exception as e:
        logger.error(f"Error saving configuration: {e}")
