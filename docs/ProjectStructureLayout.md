# Project Structure
```
accessible-boardgames/
├── main.py
├── README.md
├── requirements.txt
├── pyvenv.cfg
├── .gitignore

├── screens/                   # UI Layer
│   ├── main_menu.py
│   ├── game_selection.py
│   ├── game_play.py
│   ├── game_add_new.py
│   ├── settings.py
│   └── base_screen.py

├── logic/                     # Logic Layer (renamed from modules)
│   ├── game_manager.py        # Formerly game_loader.py
│   └── card_mapper.py         # Formerly card_scanner.py, renamed for clarity

├── services/                  # Hardware / External Interfaces
│   ├── nfc_reader.py          # Formerly nfc_handler.py
│   ├── tts_service.py         # Formerly voice_reader.py
│   └── speech_to_text.py      # Formerly voice_recognizer.py

├── navigation/
│   └── screen_manager.py

├── utils/
│   └── config.py

├── templates/                 # GameTemplates format only (not IP content)
│   └── schema.json            # Optional: JSON Schema or example format

├── user_data/                 # Per-user game progress & NFC mappings
│   ├── mappings.json
│   └── saved_games/

├── docs/
│   └── UserFlow.jpg

├── build/
│   └── buildozer.spec         # Build config moved here

└── tests/                     # (Optional) for unit/integration tests
    └── test_game_manager.py
```


---

## Explanation

- **screens/**: Contains Kivy UI screen modules.
- **logic/**: Core game logic and management (renamed from `modules/` for clarity).
- **services/**: Hardware interfaces and external services like NFC, text-to-speech, speech recognition.
- **navigation/**: Screen manager to control UI flow.
- **utils/**: Shared utilities such as configuration helpers.
- **templates/**: Holds only abstract schema or template formats — no actual IP content.
- **user_data/**: Stores per-user data like NFC mappings and saved games. Not bundled with the app.
- **docs/**: Documentation assets.
- **build/**: Build-related configuration files.
- **tests/**: Optional folder for automated tests.

---
