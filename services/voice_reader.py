# services/voice_reader.py

import multiprocessing
import pyttsx3

_current_voice_index = 0

# Define preferred voices by language
preferred_voices = {
    "en": "zira",
    "pl": "paulina"
}

def set_voice_for_language(lang_code):
    global _current_voice_index

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.stop()

    target_voice_name = preferred_voices.get(lang_code, "").lower()

    for i, voice in enumerate(voices):
        if target_voice_name in voice.name.lower():
            _current_voice_index = i
            print(f"[Voice] Set to {lang_code.upper()}: {voice.name}")
            return

    _current_voice_index = 0
    print(f"[Voice] Fallback to: {voices[0].name}")


def _speak(text, voice_index):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    if 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    print(f"[TTS] Speaking: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def speak(text):
    global _current_voice_index
    p = multiprocessing.Process(target=_speak, args=(text, _current_voice_index))
    p.start()


# VERSION which works multiple voices but doesnt work inside settings
# import threading
# import pyttsx3
#
# _current_voice_index = 0
#
# def set_voice_for_language(lang_code):
#     global _current_voice_index
#
#     engine = pyttsx3.init()
#     voices = engine.getProperty("voices")
#     engine.stop()
#
#     for i, voice in enumerate(voices):
#         if lang_code == 'en' and 'english' in voice.name.lower():
#             _current_voice_index = i
#             print(f"[Voice] Set to English: {voice.name}")
#             return
#         elif lang_code == 'pl' and 'polish' in voice.name.lower():
#             _current_voice_index = i
#             print(f"[Voice] Set to Polish: {voice.name}")
#             return
#
#     _current_voice_index = 0
#     print(f"[Voice] Fallback to: {voices[0].name}")
#
# def _speak(text, voice_index):
#     try:
#         engine = pyttsx3.init()
#         voices = engine.getProperty("voices")
#         engine.setProperty('voice', voices[voice_index].id)
#         engine.setProperty('rate', 150)
#         engine.setProperty('volume', 1.0)
#         print(f"[TTS] Speaking: {text}")
#         engine.say(text)
#         engine.runAndWait()
#         engine.stop()
#         print("[TTS] Done speaking")
#     except Exception as e:
#         print(f"[TTS] Error: {e}")
#
# def speak(text):
#     global _current_voice_index
#     thread = threading.Thread(target=_speak, args=(text, _current_voice_index), daemon=True)
#     thread.start()
