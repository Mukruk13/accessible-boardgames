# logic/commands/set_voice_volume.py

from services.voice_reader_windows import voice_reader_windows


def set_voice_volume(percent: int) -> None:
    voice_reader_windows.set_voice_volume(percent)
