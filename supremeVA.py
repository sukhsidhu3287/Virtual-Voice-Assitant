from time import struct_time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


##this function output the voice 
def bolo_g(audio):
    engine.say(audio)
    engine.runAndWait()


##takes voice input from user and writes it as a string output
def Hukam_mere_aka():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" listening / सुन रहा है ...")
        # r.pause_threshold=1
        ## time in seconds while waiting for user to speak and beafore completing the command .
        # r.energy_threshold = 200
        ## loudnes or enregyb of sound it can hear
        audio = r.listen(source)

    ## try is same as if but it can handle error that can occur

    try:
        print(" Recognizing / प्रसंस्करण .. ")
        query = r.recognize_google(audio, language = 'en-in')
        ##using google engine for speech recognization --
        print(" - ",query) ## or print(f" - {query}/n")
    except Exception:
        # print(e)
        print("sorry , I can not understand that ")
        return "None"
    return query

## wishing the user according to time
def wishuser():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        bolo_g("Good Morning Sir ")
    elif hour>=12 and hour<18:
        bolo_g("Good Afternoon Sir ")
    else:
        bolo_g("Good evening Sir ")

    bolo_g("I am your virtual assistant  how can i help you ")



if __name__ == "__main__":
    bolo_g("Supreme VA welcomes you    ")
    wishuser()
    while True:
        query = Hukam_mere_aka().lower()
        ## executing tasks based on querirs;

        if 'wikipedia' in query:
            bolo_g('please wait for few seconds')
            query = query.replace("wikipedia","")
            resutls = wikipedia.summary(query,sentences=2)
            print("Here is what i found on wikipedia  ")
            bolo_g("Here is what i found on wikipedia  ")
        #speaking and printing the results obtained from wikipedia
            print(resutls)
            bolo_g(resutls)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode .com")

        elif 'play music' in query:
            music_dir = 'music' #enter the diractory in which music is present
            #listing all songs
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))#will play 0th song;
            # we can generate random number using random function in python and play that random song

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") #converting time into string format
            bolo_g(f"time is {strtime}") #using f strings in python

        elif 'open code' in query:
            path = "C:\\Users\\sukhd\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'exit' in query:
            bolo_g(" ok sir , goodbye")
            break

    
    exit()
