# screens/settings/settings_screen.py

from typing import Any

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

from screens.base_screen import BaseScreen
from screens.settings.navigation_section import NavigationSection
from screens.settings.accessibility_section import AccessibilitySection
from screens.settings.language_section import LanguageSection
from screens.settings.back_section import BackSection


class SettingsScreen(BaseScreen):
    speak_on_enter_key: str = "settings.settings_title"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self) -> None:
        self.main_layout = BoxLayout(
            orientation="vertical", padding=20, spacing=30, size_hint_y=None
        )
        self.main_layout.bind(minimum_height=self.main_layout.setter("height"))

        # Store each section in instance variables
        self.nav_section = NavigationSection(self)
        self.access_section = AccessibilitySection(self)
        self.lang_section = LanguageSection(self)
        self.back_section = BackSection(self)

        self.main_layout.add_widget(self.nav_section)
        self.main_layout.add_widget(self.access_section)
        self.main_layout.add_widget(self.lang_section)
        self.main_layout.add_widget(self.back_section)

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.main_layout)
        self.add_widget(scroll_view)

    def update_texts(self) -> None:
        self.nav_section.update_texts()
        self.access_section.update_texts()
        self.lang_section.update_texts()
        self.back_section.update_texts()
