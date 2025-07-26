# main.py

from kivy.app import App
from navigation.screen_manager import create_screen_manager


class AccessibleBoardgamesApp(App):
    def build(self):
        return create_screen_manager()


if __name__ == "__main__":
    AccessibleBoardgamesApp().run()
