import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import pyautogui
import pyjokes
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    strTime = datetime.datetime.now().strftime("%H")
    speak(
        f"Sir, it's {strTime} I am Krihu Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc123@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "tab" in query:
            pyautogui.hotkey("alt", "tab")

        # elif "sorry" in query:
        #     kit.sendwhatmsg_to_group("+919825471941","hellow",22,36)

        elif "enter" in query:
            pyautogui.press("enter")

      

        elif 'play music' in query:
            webbrowser.open(
                "https://music.youtube.com/playlist?list=PLTacIxkoxbak6P4NZm7onPTT6C-zLOBib")
            time.sleep(4)
            for i in range(2):
                pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.hotkey("alt", "tab")
            
        elif 'open setting' in query:
            pyautogui.press("win")
            pyautogui.typewrite("settings")
            pyautogui.press("enter")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("youtube is open sir")

        elif "help" in query:
            pyautogui.hotkey("win", "e")
            speak("fill explorer is open sir")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is open sir")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("stackoverflow is open sir")

        elif 'open vs' in query:
            webbrowser.open("stackoverflow.com")
            speak("youtube is open sir")


        elif 'ok nice' in query:
            webbrowser.open(
                "https://music.youtube.com/playlist?list=PLTacIxkoxbak6P4NZm7onPTT6C-zLOBib")
            time.sleep(2)
            pyautogui.hotkey("alt", "f4")
            time.sleep(2)
            pyautogui.hotkey("enter")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            codePath = "C:\\Users\\kp096\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe"
            os.startfile(codePath)

        elif 'open cmd' in query:
            os.system("start cmd")

        elif 'open your code' in query:
            codePath = "C:\\Users\\kp096\\OneDrive\\Desktop\\JARVIS\\JARVIS.py"
            os.startfile(codePath)

        elif 'open teams' in query:
            codePath = "C:\\Users\\kp096\\OneDrive\\Desktop"
            os.startfile(codePath)


 
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif "1 tab" in query:
            for i in range(1):
                pyautogui.press("tab")

        elif "2 tab" in query:

            for i in range(2):
                pyautogui.press("tab")

        elif "3 tab" in query:
            for i in range(3):
                pyautogui.press("tab")

        elif "4 tab" in query:
            for i in range(4):
                pyautogui.press("tab")
                
        elif "shutdown" in query:
            pyautogui.hotkey("win", "d")
            pyautogui.hotkey("alt", "f4")
            pyautogui.press("enter")
    
