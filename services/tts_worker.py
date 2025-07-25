#services/tts_worker.py
import sys
import pyttsx3

def main():
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

if __name__ == "__main__":
    main()
