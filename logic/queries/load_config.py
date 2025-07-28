# logic/queries/load_config.py

import logging
from utils.config_manager import ConfigManager

logger = logging.getLogger(__name__)


def load_config():
    logger.debug("Configuration loaded")
    return ConfigManager.get_instance().all()

def load_single_item(key: str, default=None):
    return ConfigManager.get_instance().get_single_item(key, default)