# logic/commands/update_config.py

import logging
from typing import Any

from utils.config_manager import ConfigManager

logger = logging.getLogger(__name__)


def update_config_item(key: str, value: Any) -> None:
    """
    Update a configuration setting and notify any subscribed listeners.

    Args:
        key (str): The configuration key to update.
        value (Any): The new value to set for the configuration key.

    Logs:
        - Info message when the config is successfully updated.
        - Error message if the update fails.
    """
    try:
        config = ConfigManager.get_instance()
        config.set(key, value)
        logger.info(f"Config updated: {key} = {value}")
    except Exception as e:
        logger.error(f"Failed to update config key '{key}': {e}")
