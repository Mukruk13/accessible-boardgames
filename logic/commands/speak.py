# logic/commands/speak.py

from services.voice_reader_windows import voice_reader_windows
from logic.queries.load_config import load_config
import logging

logger = logging.getLogger(__name__)


def speak(text: str, force: bool = False) -> None:
    """
    Attempts to speak the provided text using the configured TTS engine.

    Args:
        text (str): The text to be spoken.
        force (bool): If True, will attempt to speak even if TTS is disabled in config.
    """
    logger.info(f"[TTS] Requested to speak text ({len(text)} chars): '{text}'")
    config = load_config()
    tts_enabled = config.get("tts_enabled", True)

    if tts_enabled or force:
        try:
            voice_reader_windows.speak(text)
            logger.info(f"[TTS] Speaking succeeded")
        except Exception as e:
            logger.error(f"[TTS] Error during speaking: {e}")
    else:
        logger.info(f"[TTS] Skipped speaking because TTS is disabled")

