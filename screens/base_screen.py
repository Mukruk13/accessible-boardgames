# screens/base_screen.py

from typing import Any

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from logic.commands.set_voice import set_voice_for_language
from logic.commands.speak import speak
from logic.queries.get_translations import (
    get_translations,
    get_translation_value,
)
from logic.queries.load_config import load_config, load_single_item


class BaseScreen(Screen):
    """
    A base screen that handles language configuration, text-to-speech,
    and dynamic translation updates for UI elements.
    """

    speak_on_enter_key: str = ""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.config = load_config()  # This will persist across screen changes
        self.language = self.config.get("language", "en")
        self.lang_data: dict[str, str] = {}

    def on_pre_enter(self) -> None:
        self.update_language_context()

    def on_enter(self) -> None:
        """
        Called when the screen is entered. Optionally speaks a configured key.
        """
        if self.speak_on_enter_key:
            Clock.schedule_once(
                lambda dt: self.speak_key(
                    self.speak_on_enter_key), 0.1)

    def update_language_context(self) -> None:
        """
        Updates the current translation dictionary and refreshes UI texts.
        """
        self.lang_data = get_translations(self.language)
        if hasattr(self, "update_texts"):
            self.update_texts()

    def set_text_from_key(
            self,
            widget: Widget,
            key_path: str,
            markup: bool = False,
            bold: bool = False) -> None:
        """
        Sets the text of a widget based on a translation key.

        Args:
            widget: The widget to update (must have a 'text' property).
            key_path: The translation key to look up.
            markup: Whether to enable markup for the widget.
            bold: Whether to wrap the text in [b] bold tags.
        """
        text = get_translation_value(self.language, key_path)
        if text:
            if bold:
                text = f"[b]{text}[/b]"
            widget.text = text
            if markup:
                widget.markup = True

    def speak(self, text: str, force: bool = False) -> None:
        speak(text, tts_enabled=self.config.get("tts_enabled", True), force=force)

    def speak_key(self, key_path: str, force: bool = False) -> None:
        text = get_translation_value(self.language, key_path)
        if text:
            self.speak(text, force=force)

    def navigate_to(self, screen_name: str) -> None:
        """
        Changes the current screen to another one by name.

        Args:
            screen_name: The name of the screen to navigate to.
        """
        self.manager.current = screen_name

    def refresh(self):
        self.reload_config()
        self.apply_language()

    def reload_config(self):
        self.config = load_config()
        self.language = self.config.get("language", "en")

    def apply_language(self):
        set_voice_for_language(self.language)
        self.update_language_context()