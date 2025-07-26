# utils/config.py

import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

DEFAULT_CONFIG = {
    "language": "en",
    "tts_enabled": True,
    # Add more default settings as needed
}


def ensure_config_exists():
    """
    Creates a default config.json file if it doesn't already exist.
    """
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)


def load_config():
    """
    Loads configuration from config.json.
    If file is missing, returns default config.
    """
    ensure_config_exists()
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(new_data):
    """
    Updates and saves config.json with new data.
    Keeps existing values unless overwritten.
    """
    config = load_config()
    config.update(new_data)  # merge without losing other settings
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
