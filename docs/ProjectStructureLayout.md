# Project Structure
```
accessible-boardgames/
│
├── main.py                       # 🚀 Entry point for the app; initializes Kivy and launches the main screen
├── requirements.txt              # 📦 Lists Python dependencies required for the app (e.g. Kivy, TTS, NFC)
├── README.md                     # 📝 Project overview, installation instructions, usage, and contribution info
├── LICENSE                       # 📄 Legal terms under which the project is shared (e.g. CC BY-NC 4.0)
├── .gitignore                    # 🛑 Specifies files/folders Git should ignore (e.g. __pycache__, .env, build artifacts)
│
├── build/
│   └── buildozer.spec            # 🏗 Buildozer config for packaging the app to Android (defines permissions, requirements, etc.)
│
├── docs/                         # 📚 Optional directory for documentation, architecture diagrams, or guides
│
├── logic/                        # 🧠 Core logic for the application
│   ├── commands/                    # 🔁 Write/update operations (e.g. saving config, setting voice)
│   └── queries/                     # ❓ Read operations (e.g. loading config, getting translations)
│
├── modules/                      # 🧩 Optional: reusable components or game-specific modules (e.g. card decks, board layouts)
│
├── navigation/
│   └── screen_manager.py         # 🧭 Handles transitions between screens in the Kivy UI
│
├── screens/                      # 🖥 Kivy Screen subclasses (UI views like settings, main menu, gameplay)
│
├── services/                     # 🔌 Interfaces to external hardware/services
│   ├── nfc_handler.py               # 📶 Handles NFC tag reading/writing
│   ├── tts_worker_windows.py        # 🗣 Handles text-to-speech (TTS) playback on Windows
│   ├── voice_reader_android.py      # 🗣 Handles text-to-speech (TTS) playback on Android
│   ├── voice_reader_windows.py      # 🗣 Handles text-to-speech (TTS) playback on Windows
│   └── voice_recognizer.py          # 🎤 Handles voice command recognition
│    
└── utils/
    ├── config.json                  # 📦 Default or user-saved configuration (e.g. language, voice settings)
    ├── config.py                    # 🧰 Helper functions for loading, saving, and validating config files
    └── translations.py              # 🌍 Translation keys, display mappings, and language data for the UI
```