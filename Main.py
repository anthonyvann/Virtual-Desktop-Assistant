
import webbrowser
import os
import time
import subprocess
import json
import requests
# import wolframalpha
# from ecapture import ecapture as ec
from Voice_Assistant import *


def main():
    while True:
        speak("Tell me, how can I help you?")
        statement = takeCommand().lower()
        
        # feature 1 -- wikipedia search
        if ("wikipedia" in statement):
            searchWiki()
        
        # feature 2 -- Accessing web browsers
        elif ("open new tab" in statement):
            webbrowser.open_new_tab()
            speak("A new tab is open now")
            time.sleep(5)
        elif ("open youtube" in statement):
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")
            time.sleep(5)
        elif ("open google" in statement):
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)
        elif ("open gmail" in statement):
            webbrowser.open_new_tab("https://mail.google.com")
            speak("G-mail is open now")
            time.sleep(5)
        
        # feature 3 -- telling time
        elif ("time" in statement):
            pass
        
        # feature 4 -- featching latest news
        elif ("news" in statement):
            pass
        
        # feature 5 -- searching data from web
        elif ("search" in statement):
            pass
        
        # shutting down the program
        elif (statement in ("good bye", "ok bye", "stop")):
            speak("Shutting down now, good bye")
            break


if __name__ == "__main__":
    # main()
    pass


