# logic/commands/set_voice.py

import logging
from services.voice_reader_windows import voice_reader_windows

logger = logging.getLogger(__name__)

def set_voice_for_language(lang_code: str) -> None:
    """
    Sets the voice to the one matching the given language code.

    Args:
        lang_code (str): Language code to set voice for.
    """
    logger.debug(f"Setting voice for language code: '{lang_code}'")
    try:
        voice_reader_windows.set_voice_for_language(lang_code)
        logger.debug(f"Voice set successfully for language '{lang_code}'")
    except Exception as e:
        logger.error(f"Failed to set voice for language '{lang_code}': {e}")

