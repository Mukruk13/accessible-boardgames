# screens/game_selection.py

from typing import Any, List

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget

from screens.base_screen import BaseScreen


class GameSelectionScreen(BaseScreen):
    """
    Game selection screen that allows the user to choose already mapped game or map NFC tags for the new one.
    """

    speak_on_enter_key: str = "game_selection.game_selection"

    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the game selection screen and builds the UI.
        """
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self) -> None:
        """
        Builds the game selection interface layout and buttons.
        """
        self.layout = BoxLayout(orientation="vertical", spacing=20, padding=50)

        self.btn_play_game = Button()
        self.spinner_saved_games = Spinner()
        self.btn_new_game = Button()
        self.btn_back_to_main_menu = Button()

        self.btn_play_game.bind(
            on_release=lambda x: self.navigate_to("game_play"))
        self.spinner_saved_games.bind(text=self.on_saved_game_selected)
        self.btn_new_game.bind(
            on_release=lambda x: self.navigate_to("game_add_new"))
        self.btn_back_to_main_menu.bind(
            on_release=lambda x: self.navigate_to("main_menu")
        )

        self.layout.add_widget(self.btn_play_game)
        self.layout.add_widget(self.spinner_saved_games)
        self.layout.add_widget(self.btn_new_game)
        self.layout.add_widget(self.btn_back_to_main_menu)

        self.add_widget(self.layout)

    def update_texts(self) -> None:
        """
        Updates the button texts based on the current language setting.
        """
        self.set_text_from_key(self.btn_play_game, "game_selection.play_game")
        self.set_text_from_key(
            self.spinner_saved_games, "game_selection.saved_games"
        )  # Spinner label
        self.set_text_from_key(self.btn_new_game, "game_selection.new_game")
        self.set_text_from_key(
            self.btn_back_to_main_menu, "game_selection.back_to_main_menu"
        )

        # Populate spinner values (you can replace with real saved games)
        self.spinner_saved_games.values = self.get_saved_games()

    def on_saved_game_selected(
            self,
            spinner: Spinner,
            selected_text: str) -> None:
        """
        Handles selection from the saved games spinner.
        """
        if selected_text:
            print(f"Selected saved game: {selected_text}")
            # Navigate or load the selected game here

    def get_saved_games(self) -> List[str]:
        """
        Return a list of saved game names. Replace this with real data loading logic.
        """
        return ["Save 1", "Save 2", "Save 3"]  # Example placeholders
