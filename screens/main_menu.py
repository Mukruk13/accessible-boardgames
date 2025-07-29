# screens/main_menu.py

from typing import Any

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from screens.base_screen import BaseScreen
from logic.commands.exit_app import exit_app


class MainMenuScreen(BaseScreen):
    """
    Main menu screen that provides navigation to other parts of the app.
    """

    speak_on_enter_key: str = "main_menu.main_menu"

    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the main menu screen and builds the UI.
        """
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self) -> None:
        """
        Builds the main menu interface layout and buttons.
        """
        self.layout = BoxLayout(orientation="vertical", spacing=20, padding=50)

        self.btn_select = Button()
        self.btn_settings = Button()
        self.btn_exit = Button()
        self.btn_test_speech = Button()

        self.btn_select.bind(
            on_release=lambda x: self.navigate_to("select_game"))
        self.btn_settings.bind(
            on_release=lambda x: self.navigate_to("settings"))
        self.btn_exit.bind(on_release=self.exit_app)
        self.btn_test_speech.bind(on_release=self.test_speech)

        self.layout.add_widget(self.btn_select)
        self.layout.add_widget(self.btn_settings)
        self.layout.add_widget(self.btn_test_speech)
        self.layout.add_widget(self.btn_exit)

        self.add_widget(self.layout)

    def update_texts(self) -> None:
        """
        Updates the button texts based on the current language setting.
        """
        self.set_text_from_key(self.btn_select, "main_menu.select_game")
        self.set_text_from_key(self.btn_settings, "main_menu.settings")
        self.set_text_from_key(self.btn_exit, "main_menu.exit")
        self.set_text_from_key(self.btn_test_speech, "main_menu.test_speech")

    def exit_app(self, instance: Widget) -> None:
        """
        Exits the application after speaking a farewell message.

        Args:
            instance: The widget that triggered the action.
        """
        self.speak_key("main_menu.goodbye")
        exit_app()

    def test_speech(self, instance: Widget) -> None:
        """
        Triggers a speech test using a predefined translation key.

        Args:
            instance: The widget that triggered the action.
        """
        self.speak_key("main_menu.test")
