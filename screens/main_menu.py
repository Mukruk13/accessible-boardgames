# screens/main_menu.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
import sys

from screens.base_screen import BaseScreen
from utils.translations import translations
from utils.config import load_config
from services.voice_reader import set_voice_for_language


class MainMenuScreen(BaseScreen):
    def __init__(self, language='en', **kwargs):
        super().__init__(**kwargs)
        config = load_config()
        self.language = config.get("language", "en")
        set_voice_for_language(self.language)
        self.lang_data = translations[self.language]

        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=50)

        self.btn_select = Button()
        self.btn_settings = Button()
        self.btn_exit = Button()
        self.btn_test_speech = Button()

        self.btn_select.bind(on_release=lambda x: self.navigate_to('select_game'))
        self.btn_settings.bind(on_release=lambda x: self.navigate_to('settings'))
        self.btn_exit.bind(on_release=self.exit_app)
        self.btn_test_speech.bind(on_release=self.test_speech)

        self.layout.add_widget(self.btn_select)
        self.layout.add_widget(self.btn_settings)
        self.layout.add_widget(self.btn_test_speech)
        self.layout.add_widget(self.btn_exit)

        self.add_widget(self.layout)
        self.update_texts()

    def update_texts(self):
        self.lang_data = translations.get(self.language, translations['en'])
        self.btn_select.text = self.lang_data['select_game']
        self.btn_settings.text = self.lang_data['settings']
        self.btn_exit.text = self.lang_data['exit']
        self.btn_test_speech.text = self.lang_data['test_speech']

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.speak(self.lang_data['main_menu']), 0.1)

    def exit_app(self, instance):
        self.speak(self.lang_data['goodbye'])
        App.get_running_app().stop()
        Window.close()
        sys.exit(0)

    def test_speech(self, instance):
        self.speak(self.lang_data['test'])

    def set_language(self, lang_code):
        self.language = lang_code
        self.update_texts()
