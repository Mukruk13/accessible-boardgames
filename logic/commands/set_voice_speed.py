# logic/commands/set_voice_rate.py

from services.voice_reader_windows import voice_reader_windows


def set_voice_speed(percent: int) -> None:
    voice_reader_windows.set_voice_rate(percent)
