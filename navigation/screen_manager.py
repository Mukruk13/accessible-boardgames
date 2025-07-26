# navigation/screen_manager.py

from kivy.uix.screenmanager import ScreenManager, FadeTransition

from screens.main_menu import MainMenuScreen
from screens.game_selection import GameSelectionScreen
from screens.game_add_new import GameAddNewScreen
from screens.settings import SettingsScreen
from screens.game_play import GamePlayScreen


def create_screen_manager() -> ScreenManager:
    manager = ScreenManager(transition=FadeTransition())

    manager.add_widget(MainMenuScreen(name="main_menu"))
    manager.add_widget(GameSelectionScreen(name="select_game"))
    manager.add_widget(GameAddNewScreen(name="add_game"))
    manager.add_widget(SettingsScreen(name="settings"))
    manager.add_widget(GamePlayScreen(name="play"))

    return manager
