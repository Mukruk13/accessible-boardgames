from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from screens.main_menu import MainMenuScreen
from screens.game_selection import GameSelectionScreen
from screens.game_add_new import GameAddNewScreen
from screens.settings import SettingsScreen
from screens.game_play import GamePlayScreen

class GraNiewidomiApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(GameSelectionScreen(name='select_game'))
        sm.add_widget(GameAddNewScreen(name='add_game'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(GamePlayScreen(name='play'))
        return sm

if __name__ == '__main__':
    GraNiewidomiApp().run()
