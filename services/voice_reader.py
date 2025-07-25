# services/voice_reader.py
# services/voice_reader.py

import multiprocessing
import pyttsx3
import sys

if sys.platform.startswith("win"):
    multiprocessing.set_start_method("spawn", force=True)  # Set once at import time


class VoiceReader:
    def __init__(self):
        self.preferred_voices = {"en": "zira", "pl": "paulina"}
        self.voice_index = 0
        self._load_default_voice()

    def _load_default_voice(self):
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            engine.stop()
            if voices:
                print(f"[Voice] Default: {voices[0].name}")
        except Exception as e:
            print(f"[Voice Init Error] {e}")

    def set_voice_for_language(self, lang_code):
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            engine.stop()

            target_name = self.preferred_voices.get(lang_code, "").lower()
            for i, voice in enumerate(voices):
                if target_name in voice.name.lower():
                    self.voice_index = i
                    print(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
                    return

            # fallback
            self.voice_index = 0
            print(f"[Voice] Fallback to: {voices[0].name}")
        except Exception as e:
            print(f"[Voice Setup Error] {e}")

    def _speak(self, text, index):
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            if 0 <= index < len(voices):
                engine.setProperty("voice", voices[index].id)
            engine.setProperty("rate", 150)
            engine.setProperty("volume", 1.0)
            print(f"[TTS] Speaking: {text}")
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"[TTS Error] {e}")

    def speak(self, text):
        p = multiprocessing.Process(
            target=self._speak,
            args=(text, self.voice_index),
        )
        p.start()

voice_reader = VoiceReader()
