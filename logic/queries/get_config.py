# logic/queries/get_config.py

from typing import Any

from utils.config_manager import ConfigManager


def get_config_item(key: str, default: Any = None) -> Any:
    """
    Retrieve a configuration value by key.

    Args:
        key (str): The configuration key to look up.
        default (Any, optional): The value to return if the key is not found. Defaults to None.

    Returns:
        Any: The value associated with the given key, or the default if not found.
    """
    config = ConfigManager.get_instance()
    return config.get(key, default)


def get_full_config() -> dict:
    """
    Retrieve the entire configuration dictionary.

    Returns:
        dict: All current configuration key-value pairs.
    """
    config = ConfigManager.get_instance()
    return config.all()
