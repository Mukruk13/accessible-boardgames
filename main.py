# main.py

from kivy.app import App

from navigation.screen_manager import create_screen_manager
from logic.commands.init_config import initialize_config
from utils.app_logging import setup_logging
from utils.log_app_banner import log_app_banner


class AccessibleBoardgamesApp(App):
    def build(self):
        setup_logging(log_to_file=True)
        log_app_banner()
        initialize_config()
        return create_screen_manager()


if __name__ == "__main__":
    AccessibleBoardgamesApp().run()

