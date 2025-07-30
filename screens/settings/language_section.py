# screens/settings/language_section.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.clock import Clock

from logic.commands.update_config import update_config_item
from logic.queries.get_translations import get_language_names


class LanguageSection(BoxLayout):
    def __init__(self, screen, **kwargs):
        super().__init__(orientation="vertical", spacing=10, size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.screen = screen
        self.config = screen.config

        self.language_label = Label(markup=True, size_hint_y=None, height=30)
        self.language_spinner = Spinner(size_hint=(1, None), height=50)
        self.language_spinner.bind(text=self.set_language)

        self.add_widget(self.language_label)
        self.add_widget(self.language_spinner)

    def update_texts(self):
        self.screen.set_text_from_key(
            self.language_label, "settings.language", markup=True, bold=True
        )
        config_lang = self.config.get("language", "en")
        localized_names = get_language_names(config_lang)

        self.language_map = {
            name: code
            for code, name in localized_names.items()
            if code != self.config["language"]
        }
        self.language_spinner.values = list(self.language_map.keys())
        self.language_spinner.text = localized_names.get(
            self.config["language"], "English"
        )

    def set_language(self, spinner, language_display_name):
        code = self.language_map.get(language_display_name)
        if not code or code == self.config.get("language", "en"):
            return
        update_config_item("language", code)
        Clock.schedule_once(
            lambda dt: self.screen.speak_key("meta.language_changed"), 0.1
        )
