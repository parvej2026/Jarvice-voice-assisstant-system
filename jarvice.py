import speech_recognition as sr
import pyttsx3 
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess

#logging configeration

LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format= "[ %(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


# Activating voice from our system
a  = pyttsx3.init("sapi5")
a.setProperty('rate',170)
voices = a.getProperty("voices")
a.setProperty('voice',voices[0].id)

#this is speak function

def speak(text):
    """ this function converts voice to text
    Args:
        text

    returns:
        voice

    """
    a.say(text)
    a.runAndWait()


#this function recognize the specch and convert it to text
def takeCommand():
    """this function take commands & recognize

    return:
        text as query

    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("say that again please")
        return "None"
    
    return query


def greeting():
    hour = (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir! how are you doing")

    elif hour >= 12 and hour <= 18:
        speak("good afternoon sir! how are you doing")

    else:
        speak("good evening sir! how are you doing")


def play_music():
    music_dir ="C:\\Users\\Us\\Documents\\assingment\\jarvice voice asisstant system\\Jarvice-voice-assisstant-system\\music"
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_songs = random.choice(songs)
            speak(f"playing a random song sir! {random_songs}")
            os.startfile(os.path.join(music_dir,random_songs))
            logging.info(f"playing music:{random_songs}")

        else:
            speak("no music available in the music directory!")

    except Exception:
        speak("sorry sir ! i could not find your music folder")

greeting()

while True:
    query = takeCommand().lower()
    print(query)
    
    if "your name" in query:
        speak("my name is jarvis")
        logging.info("user asked for assisstant's name")

    elif "time" in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strtime}")
        logging.info("user asked for the current time")


    # small talk
    elif "how are you" in query:
        speak("i am functioning at full capacity sir!")
        logging.info("user asked about assisstant's well_being")


    elif "who made you" in query:
        speak("I was created by Parvej sir, a brilliant mind")
        logging.info("user asked about assisstant's creator")
    

    elif "thank you" in query:
        speak("It's my pleasure sir!,always happy to help")
        logging.info("user expressed gratitude")
    
    # google
    elif "open google" in query:
        speak("ok sir ,please type here what do you want to read ")
        webbrowser.open("google.com")
        logging.info("user requested to open google")
    
    #calculator
    elif "open calculator" in query or "calculator" in query:
        speak("opening calculator")
        subprocess.Popen("calc.exe")
        logging.info("user requested open calculator")
    
    #notepad
    elif "notepad" in query:
        speak("opening notepad")
        subprocess.Popen("notepad.exe")
        logging.info("user requested to open notepad")

    
    elif "play music" in query or "music" in query:
        play_music()

    
    #command prompt
    elif "open terminal" in query or "open cmd" in query:
        speak("opening command prompt terminal")
        subprocess.Popen("cmd.exe")
        logging.info("user requested to open command prompt")
    
    #calender
    elif "open calender" in query:
        speak("opening calender")
        webbrowser.open("https://calender.google.com")
        logging.info("user requested to open calender")

    # youtube
    elif "youtube" in query:
        speak("opening youtube for you")
        query = query.replace("youtube","")
        webbrowser.open(f"https://www.youtube.com/results? search_query={query}")
        logging.info("user requested to open youtube")
    
    #facebppk
    elif "open facebook" in query:
        speak("opening facebook")
        webbrowser.open("facebook.com")
        logging.info("user requested to open facebook")
    
    #github
    elif "open github" in query:
        speak("ok sir,opening github")
        webbrowser.open("github.com")
        logging.info("user requested to open github")
    

    #camera
    elif "open camera" in query:
        speak("opening camera right now ")
        subprocess.Popen("camera.exe")
        logging.info("user requested to open camera")


    elif "joke" in query:
        jokes = [
            "why don't programmers like nature? too many bugs.",
            "I told my computer i needed break. it said no problem, it will go to sleep.",
            "why do java developers wear glasses? becouse they don't c sharp."
        ]
        speak(random.choice(jokes))
        logging.info("user requested a joke")
    

    elif "wikipedia" in query:
        speak("searching wikipedia.")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        speak(results)
        logging.info("user requested information to wikipedia")



    #exit
    elif "exit" in query:
        speak("thankyou for your time sir! have a greatday ahead")
        logging.info("user want exited the programme")
        exit()

    else:
        speak("sorry ! i can't help with that")
        logging.info("user asked for an unsupported command")