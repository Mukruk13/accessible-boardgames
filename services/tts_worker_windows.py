# services/tts_worker_windows.py

# services/tts_worker_windows.py

import sys

import pythoncom
import pyttsx3


if not sys.platform.startswith("win"):
    raise EnvironmentError(
        "tts_worker_windows.py is only supported on Windows.")


def main() -> None:
    """
    Main function that initializes COM, sets up the TTS engine, selects the voice,
    and speaks the provided text. Intended to be launched as a subprocess.

    Expects three command-line arguments:
        1. The text to speak.
        2. The voice index to use.
        3. The voice rate (words per minute).
    """
    try:
        pythoncom.CoInitialize()  # Initialize COM for STA (Single Threaded Apartment)

        text: str = sys.argv[1]
        index: int = int(sys.argv[2])
        rate: int = int(sys.argv[3]) if len(sys.argv) > 3 else 200

        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if 0 <= index < len(voices):
            engine.setProperty("voice", voices[index].id)
        engine.setProperty("rate", rate)
        engine.setProperty("volume", 1.0)

        print(f"[TTS Worker] Speaking at {rate} WPM: {text}")
        engine.say(text)
        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print(f"[TTS Worker Error] {e}")

    finally:
        pythoncom.CoUninitialize()  # Uninitialize COM on exit


if __name__ == "__main__":
    main()
