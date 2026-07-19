# Install required packages if not already installed
!pip install -q googletrans==4.0.0-rc1 pyttsx3

from googletrans import Translator, LANGUAGES
import pyttsx3

# Initialize translator and text-to-speech engine
translator = Translator()
engine = pyttsx3.init()

# Show first 40 supported languages
print("Supported Languages (30+):\n")
count = 0
for code, lang in LANGUAGES.items():
    print(f"{code} : {lang}")
    count += 1
    if count == 40:
        break

# Choose target language
target_lang = input("\nEnter target language code (example: ta, hi, fr, es): ").strip()

print("\nType text to translate (type 'stop' to exit)\n")

while True:
    text = input("Enter text: ").strip()

    if text.lower() == "stop":
        print("Exiting...")
        break

    try:
        # Translate text
        translated = translator.translate(text, dest=target_lang)
        print("Translated:", translated.text)

        # Speak translated text
        engine.say(translated.text)
        engine.runAndWait()

    except Exception as e:
        print("Error:", e)
