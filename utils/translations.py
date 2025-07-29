# utils/translations.py

language_display_map = {
    "English": "en",
    "Polish": "pl",
    "German": "de",
    # Add more here later, e.g., "German": "de"
}

reverse_language_display_map = {v: k for k, v in language_display_map.items()}

translations = {
    "de": {
        "settings": {
            "nav_ui": "Navigation & Benutzeroberfläche",
            "back_style": "Zurück-Schaltfläche Stil",
            "font_size": "Schriftgröße",
            "accessibility": "Barrierefreiheitseinstellungen",
            "voice_speed": "Sprachgeschwindigkeit",
            "voice_volume": "Sprachlautstärke",
            "contrast": "Hoher Kontrastmodus",
            "language": "Sprache",
            "settings_title": "Einstellungen",
            "back_to_main_menu": "Zurück zum Hauptmenü",
            "tts_on": "Stimme deaktivieren",
            "tts_off": "Stimme aktivieren",
        },
        "main_menu": {
            "select_game": "Spiel auswählen",
            "settings": "Einstellungen",
            "exit": "Beenden",
            "test_speech": "Sprachtest",
            "main_menu": "Hauptmenü",
            "goodbye": "Auf Wiedersehen",
            "test": "Test",
        },
        "meta": {
            "language_changed": "Sprache auf Deutsch geändert",
            "language_names": {"de": "Deutsch", "en": "Englisch", "pl": "Polnisch"},
            "tts_turned_on": "Stimme aktiviert",
            "tts_turned_off": "Stimme deaktiviert",
        },
    },
    "en": {
        "settings": {
            "nav_ui": "Navigation & UI",
            "back_style": "Back Button Style",
            "font_size": "Font Size",
            "accessibility": "Accessibility Settings",
            "voice_speed": "Voice Speed",
            "voice_volume": "Voice Volume",
            "contrast": "High Contrast Mode",
            "language": "Language",
            "settings_title": "Settings",
            "back_to_main_menu": "Back to Main Menu",
            "tts_on": "Disable Voice",
            "tts_off": "Enable Voice",
        },
        "main_menu": {
            "select_game": "Select Game",
            "settings": "Settings",
            "exit": "Exit",
            "test_speech": "Test Speech",
            "main_menu": "Main Menu",
            "goodbye": "Goodbye",
            "test": "Test",
        },
        "meta": {
            "language_changed": "Language changed to English",
            "language_names": {"de": "German", "en": "English", "pl": "Polish"},
            "tts_turned_on": "Voice Turned On",
            "tts_turned_off": "Voice Turned Off",
        },
    },
    "pl": {
        "settings": {
            "nav_ui": "Nawigacja i interfejs",
            "back_style": "Styl przycisku Wstecz",
            "font_size": "Rozmiar czcionki",
            "accessibility": "Ustawienia dostępności",
            "voice_speed": "Szybkość głosu",
            "voice_volume": "Głośność",
            "contrast": "Tryb wysokiego kontrastu",
            "language": "Język",
            "settings_title": "Ustawienia",
            "back_to_main_menu": "Powrót do menu głównego",
            "tts_on": "Wyłącz Głos",
            "tts_off": "Włącz Głos",
        },
        "main_menu": {
            "select_game": "Wybierz grę",
            "settings": "Ustawienia",
            "exit": "Wyjście",
            "test_speech": "Test mowy",
            "main_menu": "Menu główne",
            "goodbye": "Do widzenia",
            "test": "Test",
        },
        "meta": {
            "language_changed": "Wybrano język polski",
            "language_names": {"de": "Niemiecki", "en": "Angielski", "pl": "Polski"},
            "tts_turned_on": "Głos Włączony",
            "tts_turned_off": "Głos Wyłączony",
        },
    },
}
