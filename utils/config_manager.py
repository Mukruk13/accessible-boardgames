import json
from pathlib import Path


class ConfigManager:
    _instance = None

    DEFAULT = {
        "language": "en",
        "tts_enabled": True
    }

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ConfigManager()
        return cls._instance

    def __init__(self):
        self._config_path = Path("utils/config.json")
        self.ensure_config_exists()
        self._config = self._load()

    def ensure_config_exists(self) -> None:
        if not self._config_path.exists():
            with self._config_path.open("w", encoding="utf-8") as f:
                json.dump(self.DEFAULT.copy(), f, indent=4)

    def _load(self):
        with self._config_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, config):
        with self._config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        self._config = config

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        if self._config.get(key) != value:
            self._config[key] = value
            self._save(self._config)

    def all(self):
        return self._config

    def get_single_item(self, key, default=None):
        if self._config_path.exists():
            with self._config_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get(key, default)
        return self.DEFAULT.get(key, default)
