#services/tts_worker.py
import sys
import pyttsx3
import pythoncom

def main():
    try:
        pythoncom.CoInitialize()  # Initialize COM for STA

        text = sys.argv[1]
        index = int(sys.argv[2])

        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        if 0 <= index < len(voices):
            engine.setProperty("voice", voices[index].id)
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)

        print(f"[TTS Worker] Speaking: {text}")
        engine.say(text)
        engine.runAndWait()

        engine.stop()

    except Exception as e:
        print(f"[TTS Worker Error] {e}")

    finally:
        pythoncom.CoUninitialize()  # Uninitialize COM

if __name__ == "__main__":
    main()
