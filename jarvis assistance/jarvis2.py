from tkinter.filedialog import Open
from urllib import request
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import random
import subprocess as sp
# import pywhatkit as kit
engine = pyttsx3.init('sapi5') # speech api ---> gives output on the speak 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

{
  "ip": "117.214.111.199"
}
def find_my_ip():
    ip_address = request.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hi i am your personal assistant sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('2020543479.aman@ug.sharda.ac.in', '200101047')
    server.sendmail('2020543479.aman@ug.sharda.ac.in', to, content)
    server.close()
# defining various systems

def open_cmd():
    os.system('start cmd')

def play_on_youtube(video):
    kit.playonyt(video)


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results) 
        elif 'open leetcode' in query:
            webbrowser.open('http://www.leetcode.com')
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")   
        elif "the girl who is lucky to have me " in query:
            speak("that girls name is anjali and she is very lucky to have you sir.")
        elif "open command prompt" in query:
            speak("opening command prompt.")
            open_cmd()
        
        elif 'play music' in query:
            
            music_dir = 'C:\\Users\\HP\\Desktop\\all major works\\FULL STACK WEB DEVELOPER\\projects\\spotify_cloning\\songs'
            songs = os.listdir(music_dir)
            r = random.randint(0,len(songs)-1)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[r]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            # target 
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open camera' in query:
            speak("opening the camera sir ....")
            open_camera()

        elif 'email to aman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "2020543479.aman@ug.sharda.ac.in"    
                sendEmail(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry sir! I am not able to send this email")  

        elif 'IP address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')



        elif 'close yourself' in query:
            speak("nice meeting you sir")
            exit() 
