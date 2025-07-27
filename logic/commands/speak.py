# logic/commands/speak.py

from services.voice_reader_windows import voice_reader_windows
import logging

logger = logging.getLogger(__name__)


def speak(text: str, tts_enabled: bool = True, force: bool = False) -> None:
    """
    Attempts to speak the provided text using the configured TTS engine.

    Args:
        text (str): The text to be spoken.
        tts_enabled (bool): Whether TTS is enabled in current config.
        force (bool): If True, will attempt to speak even if TTS is disabled.
    """
    logger.info(f"[TTS] Requested to speak text ({len(text)} chars): '{text}'")

    if tts_enabled or force:
        try:
            voice_reader_windows.speak(text)
            logger.info("[TTS] Speaking succeeded")
        except Exception as e:
            logger.error(f"[TTS] Error during speaking: {e}")
    else:
        logger.info("[TTS] Skipped speaking because TTS is disabled")
