import requests
import sys
import threading
from subprocess import Popen

sys.path.append('../')
from utils.decorators import singleton

@singleton
class TextToSpeech():
    def __init__(self):
        self.language = 'en-US'


    def speak(self, text):
        threading.Thread(
            target=self.runSpeakThread, 
            args=(text,)
        ).start()

    def runSpeakThread(self, text):
        sProcess = Popen(['pico2wave','-l',self.language,'-w','file_temp.wav','"'+text+'"'])
        sProcess.wait()
        Popen(['paplay','file_temp.wav'])