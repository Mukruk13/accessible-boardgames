# screens/base_screen.py

from kivy.uix.screenmanager import Screen
from logic.commands.speak import speak
from logic.commands.set_voice import set_voice_for_language
from logic.queries.load_config import load_config
from logic.queries.get_translations import get_translations
from kivy.clock import Clock


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.language = "en"  # default
        self.lang_data = {}

    def on_pre_enter(self):
        config = load_config()
        self.language = config.get("language", "en")
        set_voice_for_language(self.language)
        self.update_language_context()

    def on_enter(self):
        if self.speak_on_enter_key:
            Clock.schedule_once(lambda dt: self.speak_key(self.speak_on_enter_key), 0.1)

    def update_language_context(self):
        self.lang_data = get_translations(self.language)
        if hasattr(self, "update_texts"):
            self.update_texts()

    def speak(self, text):
        speak(text)

    def speak_key(self, key):
        text = self.lang_data.get(key)
        if text:
            self.speak(text)

    def navigate_to(self, screen_name):
        self.manager.current = screen_name

