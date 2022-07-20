import speech_recognition as sr
import pyttsx3
import datetime
import os
import time

print('Loading...')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading...")
wishMe()


if __name__=='__main__':


    while True:
        speak("What would you like to say ")
        print("What would you like to say ")
        statement = takeCommand().lower()
        if statement==0:
            continue
        elif "bye" in statement or "stop" in statement:
            speak(' shutting down,Good bye')
            print(' shutting down,Good bye')
            break

        if "died" in statement or "lonely" in statement or "disappointed" in statement or "hopeless" in statement or "grieved" in statement or "unhappy" in statement or "sorrow" in statement or "bleak" in statement or "wistful" in statement or "sorrowful" in statement or "melancholy" in statement or "homesick" in statement or "gloomy" in statement:
            speak('Sad')
            print('Sad 😔')
            
        elif "lost" in statement or "troubled" in statement or "resigned" in statement or "miserable" in statement or "dead" in statement:
            print('Sad 😔')
            speak('Sad')


        elif "annoyed" in statement or "frustrated" in statement or "infuriated" in statement or "irritated" in statement or "mad" in statement or "vengeful" in statement or "insulted" in statement:
            speak('Angry')
            print('Angry 😡')

        elif "agitated" in statement or "fed up" in statement or "outraged" in statement or "raging" in statement or "furious" in statement or "Bitter" in statement "fumed" in statement "uptight" in statement "offended" in statement "resentful" in statement "blow up" in statement:
            speak('angry')
            print('angry 😡')

        elif "uncomfortable" in statement or "disturbed" in statement or "dislike" in statement or "revulsion" in statement:
            speak('disgust')
            print("disgust 🤢")

        elif "displease" in statement or "nauseate" in statement or "irk" in statement or "repulse" in statement "distasteful" in statement "yuck" in statement "nausea" in statement:
            speak('disgust')
            print("disgust 🤢")

        elif "amused" in statement or "glad" in statement or "pleased" in statement or "charmed" in statement or "pleased" in statement or "greatful" in statement or "joyful" in statement or "bliss" in statement or "contentment" in statement or "delight" in statement or "pleasure" in statement or "cheer" in statement or "optimism" in statement or "laughter" in statement or "laugh" in statement or "smile" in statement or "well being" in statement or "ecstacy" in statement or "paradise" in statement or "glad" in statement or "gladness" in statement or "cheerfullness" in statement or "rejoicing" in statement: 
            speak('happy')
            print('happy 😊')

        elif "worried" in statement or "terrified" in statement or "panicked" or "horrified" in statement or "desperate" in statement or "scared" in statement or "stressed" in statement:
            speak('Fear')
            print('Fear 😨')
time.sleep(3)
