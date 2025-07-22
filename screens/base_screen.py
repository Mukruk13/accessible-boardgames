# screens/base_screen.py

from kivy.uix.screenmanager import Screen
from services.voice_reader import speak


class BaseScreen(Screen):
    def speak(self, text):
        speak(text)

    def navigate_to(self, screen_name):
        self.manager.current = screen_name
