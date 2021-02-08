import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def processCommand():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command

            else:
                command = ''
                return command

    except:
        pass

    return ''

def run():
    command = processCommand()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is' + time)
    elif 'who is' in command:
        search = command.replace('who is','')
        info = wikipedia.summary(search, 2)
        talk(info)
    elif 'shut down' in command:
        talk(" Alexa going to shut down, Good Bye")
        exit()

    else:
        talk('command not recognize')
        talk('Please say a valid command')

while True:
    run()
