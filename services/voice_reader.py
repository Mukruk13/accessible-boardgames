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
        self._load_default_voice()

    def _load_default_voice(self):
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            engine.stop()
            if voices:
                print(f"[Voice] Default: {voices[0].name}")
        except Exception as e:
            print(f"[Voice Init Error] {e}")

    def set_voice_for_language(self, lang_code):
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty("voices")
            engine.stop()

            target_name = self.preferred_voices.get(lang_code, "").lower()
            for i, voice in enumerate(voices):
                if target_name in voice.name.lower():
                    self.voice_index = i
                    print(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
                    return

            self.voice_index = 0
            print(f"[Voice] Fallback to: {voices[0].name}")
        except Exception as e:
            print(f"[Voice Setup Error] {e}")

    def speak(self, text):
        python_executable = sys.executable
        tts_worker_path = os.path.join(os.path.dirname(__file__), "tts_worker.py")
        cmd = [python_executable, tts_worker_path, text, str(self.voice_index)]
        if sys.platform.startswith("win"):
            subprocess.Popen(cmd, creationflags=CREATE_NO_WINDOW)
        else:
            subprocess.Popen(cmd)

voice_reader = VoiceReader()
