import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
def speak(text):
    alexa.say(text)
    alexa.runAndWait()


def speak_to_alexa():
    try:
        with sr.Microphone() as source:
            print('Alexa is listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        print('not done')
        pass
    return command

def actions():
    command=speak_to_alexa()
    if 'play' in command:
        song=command.replace('play','')
        speak('playing '+song)
        pywhatkit.playonyt(song)
    
    elif 'who is' in command:
        person=command.replace('who is','')
        res=wikipedia.summary(person,1)
        print(res)
        speak(res)
    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('time is'+time)
    
    else:
        speak('please repeat the command')


while True:
    actions()
