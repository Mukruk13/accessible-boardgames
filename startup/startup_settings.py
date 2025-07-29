#startup/startup_settings_applier.py

import logging
from logic.queries.get_config import get_config_item
from logic.commands.set_voice_speed import set_voice_speed
from logic.commands.set_voice import set_voice_for_language
from logic.commands.set_voice_volume import set_voice_volume


class StartupSettingsApplier:
    def __init__(self, get_config):
        self.get_config = get_config
        self.logger = logging.getLogger(__name__)

    def apply_all(self):
        try:
            self._apply_language()
            self._apply_tts_enabled()
            self._apply_voice_volume()
            self._apply_voice_speed()
        except Exception as e:
            self.logger.error(f"Failed to apply startup settings: {e}")

    def _apply_language(self):
        language = self.get_config("language", "en")
        set_voice_for_language(language)
        self.logger.info(f"Language set to {language}")

    def _apply_tts_enabled(self):
        tts_enabled = self.get_config("tts_enabled", True)
        self.logger.info(f"TTS enabled: {tts_enabled}")

    def _apply_voice_volume(self):
        volume_percent = self.get_config("voice_volume_percent", 100)
        set_voice_volume(volume_percent)
        self.logger.info(f"Voice volume set to {volume_percent}%")

    def _apply_voice_speed(self):
        voice_speed = self.get_config("voice_rate_percent", 100)
        set_voice_speed(voice_speed)
        self.logger.info(f"Voice speed set to {voice_speed}")


startup_settings_applier = StartupSettingsApplier(get_config_item)
