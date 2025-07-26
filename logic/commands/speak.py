# logic/commands/speak.py

from services.voice_reader_windows import voice_reader_windows
from logic.queries.load_config import load_config
import logging

logger = logging.getLogger(__name__)


def speak(text: str) -> None:
    """
    Attempts to speak the provided text using the configured TTS engine.

    Logs the request, success, failure, or if TTS is disabled.

    Args:
        text (str): The text to be spoken.
    """
    logger.info(f"[TTS] Requested to speak text ({len(text)} chars): '{text}'")
    config = load_config()
    if config.get("tts_enabled", True):
        try:
            voice_reader_windows.speak(text)
            logger.info(f"[TTS] Speaking succeeded")
        except Exception as e:
            logger.error(f"[TTS] Error during speaking: {e}")
    else:
        logger.info(f"[TTS] Skipped speaking because TTS is disabled")
