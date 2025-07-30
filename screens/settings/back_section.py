# screens/settings/back_section.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BackSection(BoxLayout):
    def __init__(self, screen, **kwargs):
        super().__init__(orientation="vertical", spacing=10, size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.screen = screen

        self.back_button = Button(size_hint=(1, None), height=50)
        self.back_button.bind(
            on_release=lambda instance: self.screen.navigate_to("main_menu")
        )

        self.add_widget(self.back_button)

    def update_texts(self):
        self.screen.set_text_from_key(
            self.back_button, "settings.back_to_main_menu")
