# services/voice_reader.py
import multiprocessing
import pyttsx3
import sys

_current_voice_index = 0

preferred_voices = {"en": "zira", "pl": "paulina"}

if sys.platform.startswith("win"):
    multiprocessing.set_start_method("spawn", force=True)  # Move this once to module-level

def set_voice_for_language(lang_code):
    global _current_voice_index
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    target_voice_name = preferred_voices.get(lang_code, "").lower()
    for i, voice in enumerate(voices):
        if target_voice_name in voice.name.lower():
            _current_voice_index = i
            print(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
            return

    _current_voice_index = 0
    print(f"[Voice] Fallback to: {voices[0].name}")

def _speak(text, voice_index):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if 0 <= voice_index < len(voices):
            engine.setProperty("voice", voices[voice_index].id)
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        print(f"[TTS] Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"[TTS Error] {e}")

def internal_speak(text):
    global _current_voice_index
    p = multiprocessing.Process(
        target=_speak,
        args=(text, _current_voice_index),
    )
    # p.daemon = True  # Consider removing this if you want speech to finish even if main exits
    p.start()

