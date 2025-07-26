# logic/commands/exit_app.py

import logging
import sys
from kivy.app import App
from kivy.core.window import Window

logger = logging.getLogger(__name__)

def exit_app() -> None:
    """
    Cleanly stops the Kivy app, closes the window, and exits the process.
    """
    logger.info("Exiting application...")
    try:
        App.get_running_app().stop()
        Window.close()
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error during app exit: {e}")
        # Still attempt to exit even on error
        sys.exit(1)
