# logic/commands/config_subscribe.py

from typing import Callable, Any
from utils.config_manager import ConfigManager


def subscribe_to_config_changes(callback: Callable[[str, Any], None]) -> None:
    """
    Subscribe a callback to be notified when a configuration value changes.

    Args:
        callback (Callable[[str, Any], None]):
            A function that takes two arguments: the configuration key (str) and the new value (Any).
            This function will be called whenever a config value is updated.
    """
    ConfigManager.get_instance().add_listener(callback)
