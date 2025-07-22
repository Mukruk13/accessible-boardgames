#utils/translations.py

language_display_map = {
    "English": "en",
    "Polish": "pl"
    # Add more here later, e.g., "German": "de"
}

reverse_language_display_map = {v: k for k, v in language_display_map.items()}

translations = {
    "en": {
        "nav_ui": "Navigation & UI",
        "back_style": "Back Button Style",
        "font_size": "Font Size",
        "accessibility": "Accessibility Settings",
        "voice_speed": "Voice Speed",
        "contrast": "High Contrast Mode",
        "language": "Language",
        "back_to_main_menu": "Back to Main Menu",
        "settings_title": "Settings",
        "language_changed": "Language changed to English",

        # Main menu translations
        "select_game": "Select Game",
        "settings": "Settings",
        "exit": "Exit",
        "test_speech": "Test Speech",
        "main_menu": "Main Menu",
        "goodbye": "Goodbye",
        "test": "test"
    },
    "pl": {
        "nav_ui": "Nawigacja i interfejs",
        "back_style": "Styl przycisku Wstecz",
        "font_size": "Rozmiar czcionki",
        "accessibility": "Ustawienia dostępności",
        "voice_speed": "Szybkość głosu",
        "contrast": "Tryb wysokiego kontrastu",
        "language": "Język",
        "back_to_main_menu": "Powrót do menu głównego",
        "settings_title": "Ustawienia",
        "language_changed": "Wybrano język polski",

        # Main menu translations
        "select_game": "Wybierz grę",
        "settings": "Ustawienia",
        "exit": "Wyjście",
        "test_speech": "Test mowy",
        "main_menu": "Menu główne",
        "goodbye": "Do widzenia",
        "test": "test"
    }
}

