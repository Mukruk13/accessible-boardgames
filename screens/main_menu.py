# screens/main_menu.py

from screens.base_screen import BaseScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

import sys

from logic.queries.get_translations import get_translations


class MainMenuScreen(BaseScreen):
    speak_on_enter_key = "main_menu"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        self.layout = BoxLayout(orientation="vertical", spacing=20, padding=50)

        self.btn_select = Button()
        self.btn_settings = Button()
        self.btn_exit = Button()
        self.btn_test_speech = Button()

        self.btn_select.bind(on_release=lambda x: self.navigate_to("select_game"))
        self.btn_settings.bind(on_release=lambda x: self.navigate_to("settings"))
        self.btn_exit.bind(on_release=self.exit_app)
        self.btn_test_speech.bind(on_release=self.test_speech)

        self.layout.add_widget(self.btn_select)
        self.layout.add_widget(self.btn_settings)
        self.layout.add_widget(self.btn_test_speech)
        self.layout.add_widget(self.btn_exit)

        self.add_widget(self.layout)

    def update_texts(self):
        self.lang_data = get_translations(self.language)
        self.btn_select.text = self.lang_data["select_game"]
        self.btn_settings.text = self.lang_data["settings"]
        self.btn_exit.text = self.lang_data["exit"]
        self.btn_test_speech.text = self.lang_data["test_speech"]

    def exit_app(self, instance):
        self.speak(self.lang_data["goodbye"])
        App.get_running_app().stop()
        Window.close()
        sys.exit(0)

    def test_speech(self, instance):
        self.speak(self.lang_data["test"])
