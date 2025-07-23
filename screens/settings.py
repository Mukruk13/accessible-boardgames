# screens/settings.py

from screens.base_screen import BaseScreen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.uix.button import Button

from services.voice_reader import speak, set_voice_for_language

from utils.translations import (
    translations,
    language_display_map,
    reverse_language_display_map,
)
from utils.config import save_config, load_config


class SettingsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        config = load_config()
        self.selected_language = config.get("language", "en")
        self.lang_data = translations.get(
            self.selected_language, translations["en"])

        self.main_layout = BoxLayout(
            orientation="vertical", padding=20, spacing=30)
        self.add_widget(self.main_layout)
        self.build_ui()

    def on_enter(self):
        Clock.schedule_once(
            lambda dt: self.speak(self.lang_data["settings_title"]), 0.1
        )

    def build_ui(self):
        self.main_layout.clear_widgets()

        # Navigation & UI Section
        self.nav_ui_label = Label(markup=True)
        self.back_style_label = Label()
        self.font_size_label = Label()
        nav_ui_section = BoxLayout(orientation="vertical", spacing=10)
        nav_ui_section.add_widget(self.nav_ui_label)
        nav_ui_section.add_widget(self.back_style_label)
        nav_ui_section.add_widget(self.font_size_label)

        # Accessibility Settings
        self.accessibility_label = Label(markup=True)
        self.voice_speed_label = Label()
        self.contrast_label = Label()
        accessibility_section = BoxLayout(orientation="vertical", spacing=10)
        accessibility_section.add_widget(self.accessibility_label)
        accessibility_section.add_widget(self.voice_speed_label)
        accessibility_section.add_widget(self.contrast_label)

        # Language Section
        self.language_label = Label(markup=True)
        display_name = reverse_language_display_map.get(
            self.selected_language, "English"
        )
        self.language_spinner = Spinner(
            text=display_name,
            values=list(language_display_map.keys()),
            size_hint=(1, None),
            height=50,
        )
        self.language_spinner.bind(text=self.set_language)

        language_section = BoxLayout(orientation="vertical", spacing=10)
        language_section.add_widget(self.language_label)
        language_section.add_widget(self.language_spinner)

        # Back Button Section
        self.back_button = Button(size_hint=(1, None), height=50)
        self.back_button.bind(
            on_release=lambda instance: self.navigate_to("main_menu"))

        back_button_section = BoxLayout(orientation="vertical", spacing=10)
        back_button_section.add_widget(self.back_button)

        # Assemble sections
        self.main_layout.add_widget(nav_ui_section)
        self.main_layout.add_widget(accessibility_section)
        self.main_layout.add_widget(language_section)
        self.main_layout.add_widget(back_button_section)

        self.update_texts()

    def update_texts(self):
        self.lang_data = translations.get(
            self.selected_language, translations["en"])

        self.nav_ui_label.text = f"[b]{self.lang_data['nav_ui']}[/b]"
        self.back_style_label.text = self.lang_data["back_style"]
        self.font_size_label.text = self.lang_data["font_size"]

        self.accessibility_label.text = f"[b]{self.lang_data['accessibility']}[/b]"
        self.voice_speed_label.text = self.lang_data["voice_speed"]
        self.contrast_label.text = self.lang_data["contrast"]

        self.language_label.text = f"[b]{self.lang_data['language']}[/b]"
        self.language_spinner.text = reverse_language_display_map.get(
            self.selected_language, "English"
        )
        self.back_button.text = self.lang_data["back_to_main_menu"]

    def set_language(self, spinner, language_name):
        lang_code = language_display_map.get(language_name)
        if not lang_code:
            print(f"Unsupported language: {language_name}")
            return

        self.selected_language = lang_code
        set_voice_for_language(lang_code)
        save_config({"language": lang_code})

        if self.manager:
            try:
                main_menu = self.manager.get_screen("main_menu")
                main_menu.set_language(lang_code)
            except Exception as e:
                print(f"Main menu screen not found or error: {e}")

        Clock.schedule_once(
            lambda dt: self.speak(self.lang_data["language_changed"]), 0.1
        )
        self.update_texts()
