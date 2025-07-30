# services/voice_reader_windows.py

import logging
import os

import subprocess
import sys
from typing import List

logger = logging.getLogger(__name__)
logging.getLogger("comtypes").setLevel(logging.CRITICAL)

if not sys.platform.startswith("win"):
    logger.error("voice_reader_windows.py is only supported on Windows.")
    raise EnvironmentError(
        "voice_reader_windows.py is only supported on Windows.")

CREATE_NO_WINDOW = 0x08000000


class VoiceReaderWindows:
    """
    VoiceReaderWindows provides a simple text-to-speech interface using pyttsx3 on Windows.
    It supports setting a preferred voice based on language and speaking text via a worker process.
    """

    def __init__(self) -> None:
        """Initialize the voice reader and load available system voices."""
        self.preferred_voices: dict[str, str] = {"de": "hedda", "en": "zira", "pl": "paulina"}
        self.voice_index: int = 0
        self.voice_rate: int = 200  # pyttsx3 default is around 200 WPM
        self.voice_volume: float = 1.0  # Max volume
        self.voices: List = []
        self._load_voices_once()

    def _load_voices_once(self) -> None:
        """Load available voices from the system using pyttsx3 (only once)."""
        try:
            import pyttsx3

            engine = pyttsx3.init()
            self.voices = engine.getProperty("voices")
            if self.voices:
                logger.info(f"[Voice] Default: {self.voices[0].name}")
            engine.stop()
            del engine
        except Exception as e:
            logger.error(f"[Voice Init Error] {e}")

    def set_voice_for_language(self, lang_code: str) -> None:
        """
        Set the voice index based on the preferred voice for the given language code.

        Args:
            lang_code (str): The ISO language code, e.g., 'en' or 'pl'.
        """
        target_name = self.preferred_voices.get(lang_code, "").lower()
        for i, voice in enumerate(self.voices):
            if target_name in voice.name.lower():
                self.voice_index = i
                logger.info(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
                return

        if self.voices:
            self.voice_index = 0
            logger.warning(f"[Voice] Fallback to: {self.voices[0].name}")
        else:
            logger.error("[Voice] No voices loaded!")

    def set_voice_rate(self, percent: int) -> None:
        """
        Set the voice speed as a percentage of the default rate.

        Args:
            percent (int): Desired rate percentage (100 to 300).
        """
        percent = max(100, min(500, percent))
        self.voice_rate = int(200 * (percent / 100))
        logger.info(f"[Voice] Rate set to {self.voice_rate} WPM ({percent}%)")

    def set_voice_volume(self, percent: int) -> None:
        percent = max(0, min(100, percent))
        self.voice_volume = max(0, min(100, percent)) / 100.0
        logger.info(f"[Voice] Volume set to {self.voice_volume * 100:.0f}%")

    def speak(self, text: str) -> None:
        """
        Speak the given text using the selected voice by spawning a subprocess.

        Args:
            text (str): The text to be spoken aloud.
        """
        if not self.voices:
            logger.error("[Voice] Cannot speak. No voices available.")
            return

        python_executable = sys.executable
        tts_worker_path = os.path.join(
            os.path.dirname(__file__), "tts_worker_windows.py"
        )
        cmd = [
            python_executable,
            tts_worker_path,
            text,
            str(self.voice_index),
            str(self.voice_rate),
            str(self.voice_volume)
        ]

        subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)


# Singleton instance
voice_reader_windows = VoiceReaderWindows()
