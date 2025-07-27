# screens/settings.py

from typing import Any

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

from screens.base_screen import BaseScreen

from logic.commands.save_config import save_config
from logic.commands.set_voice import set_voice_for_language
from logic.queries.get_translations import (
    get_language_names,
    get_translations,
)
from logic.queries.load_config import load_config


class SettingsScreen(BaseScreen):
    """
    Screen for adjusting application settings including language, voice, and accessibility options.
    """

    speak_on_enter_key: str = "settings.settings_title"

    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the settings screen and builds its UI layout.
        """
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self) -> None:
        """
        Constructs the layout and components for the settings interface.
        """
        self.main_layout = BoxLayout(
            orientation="vertical", padding=20, spacing=30)

        # Navigation & UI Section
        self.nav_ui_label = Label(markup=True)
        self.back_style_label = Label()
        self.font_size_label = Label()
        nav_ui_section = BoxLayout(orientation="vertical", spacing=10)
        nav_ui_section.add_widget(self.nav_ui_label)
        nav_ui_section.add_widget(self.back_style_label)
        nav_ui_section.add_widget(self.font_size_label)

        # Accessibility Section
        self.accessibility_label = Label(markup=True)
        self.voice_speed_label = Label()
        self.contrast_label = Label()
        self.tts_toggle_button = Button(size_hint=(1, None), height=50)
        self.tts_toggle_button.bind(on_release=self.toggle_tts)
        accessibility_section = BoxLayout(orientation="vertical", spacing=10)
        accessibility_section.add_widget(self.accessibility_label)
        accessibility_section.add_widget(self.voice_speed_label)
        accessibility_section.add_widget(self.contrast_label)
        accessibility_section.add_widget(self.tts_toggle_button)

        # Language Section
        self.language_label = Label(markup=True)
        self.language_spinner = Spinner(size_hint=(1, None), height=50)
        self.language_spinner.bind(text=self.set_language)

        language_section = BoxLayout(orientation="vertical", spacing=10)
        language_section.add_widget(self.language_label)
        language_section.add_widget(self.language_spinner)

        # Back Button
        self.back_button = Button(size_hint=(1, None), height=50)
        self.back_button.bind(
            on_release=lambda instance: self.navigate_to("main_menu"))

        back_section = BoxLayout(orientation="vertical", spacing=10)
        back_section.add_widget(self.back_button)

        # Assemble UI
        self.main_layout.add_widget(nav_ui_section)
        self.main_layout.add_widget(accessibility_section)
        self.main_layout.add_widget(language_section)
        self.main_layout.add_widget(back_section)
        self.add_widget(self.main_layout)

    def update_texts(self) -> None:
        """
        Updates all visible labels and buttons with translated text based on the current language.
        """
        self.set_text_from_key(
            self.nav_ui_label, "settings.nav_ui", markup=True, bold=True
        )
        self.set_text_from_key(self.back_style_label, "settings.back_style")
        self.set_text_from_key(self.font_size_label, "settings.font_size")

        self.set_text_from_key(
            self.accessibility_label,
            "settings.accessibility",
            markup=True,
            bold=True)
        self.set_text_from_key(self.voice_speed_label, "settings.voice_speed")
        self.set_text_from_key(self.contrast_label, "settings.contrast")
        self.update_tts_button_label()

        self.set_text_from_key(
            self.language_label, "settings.language", markup=True, bold=True
        )
        self.set_text_from_key(self.back_button, "settings.back_to_main_menu")

        config_lang = self.config.get("language", "en")

        localized_names = get_language_names(config_lang)

        self.language_spinner.values = list(localized_names.values())
        self.language_spinner.text = localized_names.get(
            self.language, "English")

    def set_language(
            self,
            spinner: Spinner,
            language_display_name: str) -> None:
        """
        Changes the app's language based on user selection from the language spinner.

        Args:
            spinner: The spinner widget triggering the change.
            language_display_name: The display name of the selected language.
        """
        current_lang = self.config.get("language", "en")
        display_map = get_language_names(current_lang)
        reverse_map = {v: k for k, v in display_map.items()}

        lang_code = reverse_map.get(language_display_name)
        if not lang_code or lang_code == self.language:
            return

        self.language = lang_code
        self.lang_data = get_translations(self.language)

        save_config({"language": lang_code})
        self.config["language"] = lang_code
        set_voice_for_language(lang_code)
        self.update_texts()

        Clock.schedule_once(
            lambda dt: self.speak_key("meta.language_changed"), 0.1)

    def toggle_tts(self, instance) -> None:
        """
        Toggles the Text-to-Speech feature on or off and saves it to config.
        """
        current_state = self.config.get("tts_enabled", True)
        new_state = not current_state

        self.config["tts_enabled"] = new_state
        save_config(self.config)

        self.update_tts_button_label()
        status_key = "meta.tts_turned_on" if new_state else "meta.tts_turned_off"
        Clock.schedule_once(lambda dt: self.speak_key(status_key, force=True), 0.1)

    def update_tts_button_label(self) -> None:
        """
        Updates the TTS toggle button label to reflect the current state.
        """
        is_enabled = self.config.get("tts_enabled", True)

        label_key = "settings.tts_on" if is_enabled else "settings.tts_off"
        self.set_text_from_key(self.tts_toggle_button, label_key)
