# commands/speak.py

from services.voice_reader import internal_speak
from logic.queries.load_config import load_config

def speak(text):
    config = load_config()
    if config.get("tts_enabled", True):
        internal_speak(text)
    else:
        print(f"[TTS] Skipped speaking because TTS is disabled: {text}")
