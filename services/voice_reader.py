# services/voice_reader.py

import sys
import subprocess
import os

if sys.platform.startswith("win"):
    CREATE_NO_WINDOW = 0x08000000
else:
    CREATE_NO_WINDOW = 0

class VoiceReader:
    def __init__(self):
        self.preferred_voices = {"en": "zira", "pl": "paulina"}
        self.voice_index = 0
        self.voices = []
        self._load_voices_once()

    def _load_voices_once(self):
        try:
            import pyttsx3
            engine = pyttsx3.init()
            self.voices = engine.getProperty("voices")
            if self.voices:
                print(f"[Voice] Default: {self.voices[0].name}")
            engine.stop()
            # Dispose engine explicitly if needed:
            del engine
        except Exception as e:
            print(f"[Voice Init Error] {e}")

    def set_voice_for_language(self, lang_code):
        target_name = self.preferred_voices.get(lang_code, "").lower()
        for i, voice in enumerate(self.voices):
            if target_name in voice.name.lower():
                self.voice_index = i
                print(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
                return

        # fallback if not found
        if self.voices:
            self.voice_index = 0
            print(f"[Voice] Fallback to: {self.voices[0].name}")
        else:
            print("[Voice] No voices loaded!")

    def speak(self, text):
        python_executable = sys.executable
        tts_worker_path = os.path.join(os.path.dirname(__file__), "tts_worker.py")

        cmd = [python_executable, tts_worker_path, text, str(self.voice_index)]
        if sys.platform.startswith("win"):
            subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)
        else:
            subprocess.Popen(cmd)

voice_reader = VoiceReader()

