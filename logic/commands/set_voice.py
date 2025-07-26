# logic/commands/set_voice.py

from services.voice_reader_windows import voice_reader_windows


def set_voice_for_language(lang_code):
    voice_reader_windows.set_voice_for_language(lang_code)
