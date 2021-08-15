import pyttsx3
import sys
import threading

sys.path.append('../')
from utils.decorators import singleton

@singleton
class TextToSpeech():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 100)


    def speak(self, text):
        threading.Thread(
            target=self.runSpeakThread, 
            args=(text,)
        ).start()

    def runSpeakThread(self, text):
        self.engine.say(text)
        self.engine.runAndWait()