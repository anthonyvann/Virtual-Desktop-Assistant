from datetime import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import time


# speech engine settup
ENGINE = pyttsx3.init("sapi5")
VOICES = ENGINE.getProperty("voices")

# setting female voice
ENGINE.setProperty("voice", "voices[1].id")



# Converts text to speech
def speak(text: str):
    ENGINE.say(text)
    print(text)
    ENGINE.runAndWait()

# Greets the user
def wishMe():
    hour = datetime.now().hour
    if (0 <= hour < 12):
        speak("Hello, good morning")
    elif (12 <= hour < 18):
        speak("Hello, good afternoon")
    else:
        speak("Hello, good evening")

# Listens for a command via human language
def takeCommand() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        audio = recognizer.listen(src)
        try:
            statement = recognizer.recognize_google(audio, language="en-in")
            print(f"Statement received: {statement}\n")
        except Exception:
            speak("Sorry, I didnt quite catch that. Can you say that again?")
            return "None"
        return statement

# Searches wikipedia for the summary of the desired topic
def searchWiki():
    speak("Searching Wikipedia...")
    statement = statement.replace("wikipedia", "")
    results = wikipedia.summary(statement, sentences=3)
    speak(f"According to Wikipedia, {results}")