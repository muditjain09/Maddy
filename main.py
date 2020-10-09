import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
Master = "Mudit"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = datetime.now().hour
    if hour > 0 and hour < 12:
        speak("Good Morning" + Master)
    elif hour > 12 and hour < 18:
        speak("Good Afternoon" + Master)
    else:
        speak("Good Evening" + Master)
    # speak("I am Maddy, how May I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        querry = r.recognize_google(audio, language="en-in")
        print(f"user said:{querry}\n")
    except Exception as e:
        print("Say the again please")
        querry = None
    return querry


speak("Initializing Maddy")
wishme()
query = takecommand()
if 'wikipedia'in query.lower():
    speak("searching wikipedia..")
    query = query.replace('wikipedia', '')
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)
elif 'open youtube' in query.lower():
    url = 'https://www.youtube.com/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'the time'in query.lower():
    strtime = datetime.now().strftime("%H:%M:%S")
    print(strtime)
    speak(f"{Master} the time is{strtime}")
elif 'open code' in query.lower():
    codepath = "C:\\Users\\jmudi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)
