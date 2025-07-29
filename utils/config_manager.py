#utils/config_manager.py

import json
from pathlib import Path
from typing import Callable, Any


class ConfigManager:
    _instance = None

    DEFAULT = {
        "language": "en",
        "tts_enabled": True,
        "voice_rate": 100,
    }

    def __init__(self):
        self._config_path = Path("utils/config.json")
        self._listeners: list[Callable[[str, Any], None]] = []

        self.ensure_config_exists()
        self._config = self._load()

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ConfigManager()
        return cls._instance

    def ensure_config_exists(self) -> None:
        if not self._config_path.exists():
            with self._config_path.open("w", encoding="utf-8") as f:
                json.dump(self.DEFAULT.copy(), f, indent=4)

    def _load(self) -> dict:
        with self._config_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, config: dict) -> None:
        with self._config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        self._config = config

    def _notify(self, key: str, value: Any) -> None:
        for callback in self._listeners:
            try:
                callback(key, value)
            except Exception as e:
                # Optionally log or handle individual callback failures
                pass

    def add_listener(self, callback: Callable[[str, Any], None]) -> None:
        if callback not in self._listeners:
            self._listeners.append(callback)

    def get(self, key: str, default=None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        if self._config.get(key) != value:
            self._config[key] = value
            self._save(self._config)
            self._notify(key, value)

    def all(self) -> dict:
        return self._config

    def get_single_item(self, key: str, default=None) -> Any:
        if self._config_path.exists():
            with self._config_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get(key, default)
        return self.DEFAULT.get(key, default)
