from intent_classification.intent_classification import IntentClassifier
import pyttsx3
import speech_recognition as sr
import sys

# assist functions
from assistant_functions.weather import get_weather
from assistant_functions.greeting import get_greeting
from assistant_functions.open_app import *
from assistant_functions.media_control import *
from assistant_functions.search import *

intent_classifier = IntentClassifier()

class Assistant(OpenApplication):

    def __init__(self, name): 
        self.name = name #Create instance variable name

        # Code for text-to-speech engine
        self.speech_engine = pyttsx3.init() 
        self.speech_engine.setProperty("rate", 150) #Speed of the voice

        self.r = sr.Recognizer() #Speech recognizer
        self.mic = sr.Microphone(device_index=0) #Change device_index 

        # self.say(f"Hello Cherish sir, I am {self.name}, here for you.")

    def leave(self, *args, **kwargs):
        self.say("Bye bye sir, have a good day.")
        sys.exit(0)

    def listen(self):
        """Uses speech_recognition library to listen to get audio input and understand what the user is saying"""
    
        with self.mic as source:
            print("listening")
            audio = self.r.listen(source, timeout=3, phrase_time_limit=5) 
        try:
            return self.r.recognize_google(audio)
        except sr.exceptions.UnknownValueError:
            return self.listen()

    def say(self, text):
        """Uses pyttsx3 engine text-to-speech to to say 'text' argument"""
        print(f"{self.name} : {text}")
        self.speech_engine.say(text)
        self.speech_engine.runAndWait()

    def reply(self, text):
        intent = intent_classifier.predict(text)
        print('intent: ', intent)

        replies = {
            'greeting': get_greeting,
            'weather': get_weather,
            'leaving': self.leave,

            'open_application': self.open_application,

            'volume_up': volume_up,
            'volume_down': volume_down,
            'mute': mute,
            'media_stop': media_stop,
            'media_prev': media_prev,
            'media_play_pause': media_play_pause,
            'media_next': media_next,
            'search': search,
            }
        try:
            reply_func = replies[intent]

            if callable(reply_func):
                reply = reply_func(text=text)
                if not reply:
                    reply = "Sure sir."
                self.say(reply) 
        except KeyError:
            self.say("sorry, i am not able to understand.")

    def main(self):
        while True:
            said = self.listen()
            print('-'*20)
            print('User: ', said)
            if f'{self.name}'.lower() in said.lower():
                self.reply(said)

if __name__ == '__main__': 
    assistant = Assistant("Jarvis") #Create an instance and name it "Assistant"
    assistant.main()






