import requests
from playsound import playsound
import sys
import threading

sys.path.append('../')
from utils.decorators import singleton

@singleton
class TextToSpeech():
    def __init__(self):
        self.default_params = {
            'INPUT_TEXT':'',
            'INPUT_TYPE':'TEXT',
            'OUTPUT_TYPE':'AUDIO',
            'LOCALE':'en_US',
            'AUDIO':'WAVE_FILE'
        }


    def speak(self, text):
        threading.Thread(
            target=self.runSpeakThread, 
            args=(text,)
        ).start()

    def runSpeakThread(self, text):
        self.default_params['INPUT_TEXT'] = text
        r = requests.get('http://localhost:59125/process',params=self.default_params)
        with open('file_temp.wav','wb') as f:
            f.write(r.content)
            playsound('file_temp.wav')