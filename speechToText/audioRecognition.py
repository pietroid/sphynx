import queue
import vosk
import json

class AudioRecognition:
    def __init__(self,samplerate):
        self.out = queue.Queue()
        self.model = vosk.Model('speechToText/stt_model')
        self.recognizer =  vosk.KaldiRecognizer(self.model, samplerate)

    def recognize(self,audioInput):
        try:
            data = audioInput.get_nowait()
            if(self.recognizer.AcceptWaveform(data)):
                result = json.loads(self.recognizer.Result())
                if(result['text'] != ''):
                    self.out.put(result)
        except: 
            pass
        return self.out