# logic/commands/speak.py

from services.voice_reader_windows import voice_reader_windows
from logic.queries.load_config import load_config


def speak(text):
    config = load_config()
    if config.get("tts_enabled", True):
        voice_reader_windows.speak(text)
    else:
        print(f"[TTS] Skipped speaking because TTS is disabled: {text}")
