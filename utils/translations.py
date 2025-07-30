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
        "game_selection": {
            "game_selection": "Spielauswahl",
            "play_game": "Spiel starten",
            "saved_games": "Gespeicherte Spiele",
            "new_game": "Neues Spiel",
            "back_to_main_menu": "Zurück zum Hauptmenü",
            "placeholder": "Placeholder",
        },
        "meta": {
            "language_changed": "Sprache auf Deutsch geändert",
            "language_names": {"de": "Deutsch", "en": "Englisch", "pl": "Polnisch"},
            "tts_turned_on": "Stimme aktiviert",
            "tts_turned_off": "Stimme deaktiviert",
            "speed_changed": "Sprachgeschwindigkeit auf {value} Prozent eingestellt",
            "volume_changed": "Sprachlautstärke auf {value} Prozent gesetzt",
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
        "game_selection": {
                    "game_selection": "Game Selection",
                    "play_game": "Play Game",
                    "saved_games": "Saved Games",
                    "new_game": "New Game",
                    "back_to_main_menu": "Back to Main Menu",
                    "placeholder": "Placeholder",
                },
        "meta": {
            "language_changed": "Language changed to English",
            "language_names": {"de": "German", "en": "English", "pl": "Polish"},
            "tts_turned_on": "Voice Turned On",
            "tts_turned_off": "Voice Turned Off",
            "speed_changed": "Voice Speed set to {value} percent",
            "volume_changed": "Voice Volume set to {value} percent"
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
        "game_selection": {
            "game_selection": "Wybór gry",
            "play_game": "Zagraj w grę",
            "saved_games": "Zapisane gry",
            "new_game": "Nowa gra",
            "back_to_main_menu": "Powrót do menu głównego",
            "placeholder": "Placeholder",
        },
        "meta": {
            "language_changed": "Wybrano język polski",
            "language_names": {"de": "Niemiecki", "en": "Angielski", "pl": "Polski"},
            "tts_turned_on": "Głos Włączony",
            "tts_turned_off": "Głos Wyłączony",
            "speed_changed": "Szybkość głosu ustawiona na {value} procent",
            "volume_changed": "Głośność ustawiona na {value} procent"
        },
    },
}
