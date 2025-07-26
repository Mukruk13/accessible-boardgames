# logic/commands/init_config.py

from utils.config import ensure_config_exists

def initialize_config():
    """
    Ensures the configuration file exists at app startup.
    """
    ensure_config_exists()
