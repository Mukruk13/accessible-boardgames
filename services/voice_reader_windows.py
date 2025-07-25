# services/voice_reader_windows.py

import os
import subprocess
import sys
from typing import List


if not sys.platform.startswith("win"):
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
        self.preferred_voices: dict[str, str] = {"en": "zira", "pl": "paulina"}
        self.voice_index: int = 0
        self.voices: List = []
        self._load_voices_once()

    def _load_voices_once(self) -> None:
        """Load available voices from the system using pyttsx3 (only once)."""
        try:
            import pyttsx3

            engine = pyttsx3.init()
            self.voices = engine.getProperty("voices")
            if self.voices:
                print(f"[Voice] Default: {self.voices[0].name}")
            engine.stop()
            del engine
        except Exception as e:
            print(f"[Voice Init Error] {e}")

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
                print(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
                return

        if self.voices:
            self.voice_index = 0
            print(f"[Voice] Fallback to: {self.voices[0].name}")
        else:
            print("[Voice] No voices loaded!")

    def speak(self, text: str) -> None:
        """
        Speak the given text using the selected voice by spawning a subprocess.

        Args:
            text (str): The text to be spoken aloud.
        """
        if not self.voices:
            print("[Voice] Cannot speak. No voices available.")
            return

        python_executable = sys.executable
        tts_worker_path = os.path.join(
            os.path.dirname(__file__), "tts_worker_windows.py"
        )
        cmd = [python_executable, tts_worker_path, text, str(self.voice_index)]

        subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)


# Singleton instance
voice_reader_windows = VoiceReaderWindows()
