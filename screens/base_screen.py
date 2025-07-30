# screens/base_screen.py

from typing import Any

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from logic.commands.config_subscribe import subscribe_to_config_changes
from logic.commands.set_voice import set_voice_for_language
from logic.commands.speak import speak
from logic.queries.get_config import get_config_item, get_full_config
from logic.queries.get_translations import get_translations, get_translation_value


class BaseScreen(Screen):
    """
    A base screen that handles language configuration, text-to-speech,
    and dynamic translation updates for UI elements.
    """

    speak_on_enter_key: str = ""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.config = get_full_config()
        self.lang_data: dict[str, str] = {}
        self._last_language: str | None = None

        # Subscribe to config changes
        subscribe_to_config_changes(self._on_config_change)

    def on_pre_enter(self) -> None:
        """
        Called just before the screen becomes visible.
        Ensures that the language context is up to date.
        """
        self._ensure_language_context_is_current()

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
        Updates the local translation dictionary and refreshes UI texts.
        """
        self.lang_data = get_translations(self.config["language"])
        if hasattr(self, "update_texts"):
            self.update_texts()

    def set_text_from_key(
        self,
        widget: Widget,
        key_path: str,
        markup: bool = False,
        bold: bool = False,
    ) -> None:
        """
        Sets the text of a widget based on a translation key.

        Args:
            widget (Widget): The widget to update (must have a 'text' property).
            key_path (str): The translation key to look up.
            markup (bool): Whether to enable markup for the widget.
            bold (bool): Whether to wrap the text in [b] bold tags.
        """
        text = get_translation_value(self.config["language"], key_path)
        if text:
            if bold:
                text = f"[b]{text}[/b]"
            widget.text = text
            if markup:
                widget.markup = True

    def speak(self, text: str, force: bool = False) -> None:
        """
        Speaks the given text using the TTS engine if enabled.

        Args:
            text (str): The text to speak.
            force (bool): If True, speaks the text regardless of config.
        """
        speak(
            text,
            tts_enabled=get_config_item(
                "tts_enabled",
                True),
            force=force)

    def speak_key(self, key_path: str, force: bool = False, **kwargs) -> None:
        """
        Speaks a translated string based on a translation key.

        Args:
            key_path (str): The translation key to speak.
            force (bool): If True, speaks the text regardless of config.
            **kwargs: Optional format arguments to inject into the translation string.
        """
        text = get_translation_value(self.config["language"], key_path)
        if text and kwargs:
            try:
                text = text.format(**kwargs)
            except KeyError as e:
                self.logger.error(
                    f"Missing format value for '{e.args[0]}' in translation '{key_path}'"
                )
        if text:
            self.speak(text, force=force)

    def navigate_to(self, screen_name: str) -> None:
        """
        Changes the current screen to another one by name.

        Args:
            screen_name (str): The name of the screen to navigate to.
        """
        self.manager.current = screen_name

    def _on_config_change(self, key: str, value: Any) -> None:
        """
        Internal handler for config changes.

        Args:
            key (str): Config key that changed.
            value (Any): New value for the key.
        """
        if key == "language":
            self._ensure_language_context_is_current()

    def _ensure_language_context_is_current(self) -> None:
        """
        Ensures that the app's current language matches the config.
        If changed, updates translations and TTS voice.
        """
        current_language = get_config_item("language", "en")
        if current_language != self._last_language:
            self.update_language_context()
            set_voice_for_language(current_language)
            self._last_language = current_language
