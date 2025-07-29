# screens/settings/navigation_section.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class NavigationSection(BoxLayout):
    def __init__(self, screen, **kwargs):
        super().__init__(orientation="vertical", spacing=10, size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.screen = screen

        self.nav_ui_label = Label(markup=True, size_hint_y=None, height=30)
        self.back_style_label = Label(size_hint_y=None, height=30)
        self.font_size_label = Label(size_hint_y=None, height=30)

        self.add_widget(self.nav_ui_label)
        self.add_widget(self.back_style_label)
        self.add_widget(self.font_size_label)

    def update_texts(self):
        self.screen.set_text_from_key(
            self.nav_ui_label, "settings.nav_ui", markup=True, bold=True
        )
        self.screen.set_text_from_key(self.back_style_label, "settings.back_style")
        self.screen.set_text_from_key(self.font_size_label, "settings.font_size")
