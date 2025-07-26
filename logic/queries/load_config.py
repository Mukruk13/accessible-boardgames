# queries/load_config.py

import logging
from utils.config import load_config as _load_config

logger = logging.getLogger(__name__)

def load_config():
    logger.debug("Configuration loaded")
    return _load_config()
