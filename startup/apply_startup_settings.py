#startup/apply_startup_settings.py

import logging

from logic.queries.get_config import get_config_item
from logic.commands.set_voice_speed import set_voice_speed

logger = logging.getLogger(__name__)


def apply_startup_settings() -> None:
    """
    Applies persisted configuration settings at application startup.

    This includes settings such as voice rate, which need to be
    applied immediately for correct behavior.
    """
    try:
        voice_rate = get_config_item("voice_rate_percent", 100)
        set_voice_speed(voice_rate)
        logger.info(f"Startup setting applied: voice_rate_percent = {voice_rate}")
    except Exception as e:
        logger.error(f"Failed to apply startup settings: {e}")
