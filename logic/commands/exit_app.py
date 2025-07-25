from kivy.app import App
from kivy.core.window import Window
import sys

def exit_app():
    App.get_running_app().stop()
    Window.close()
    sys.exit(0)
