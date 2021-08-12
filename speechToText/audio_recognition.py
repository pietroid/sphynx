import queue
import vosk

class AudioRecognition:
    def __init__(self,samplerate):
        self.out = queue.Queue()
        self.model = vosk.Model('stt_model')
        self.recognizer =  vosk.KaldiRecognizer(self.model, samplerate)

    def recognize(self,audioInput):
        try:
            data = audioInput.get_nowait()
            if(self.recognizer.AcceptWaveform(data)):
                self.out.put(self.recognizer.Result())
        except: 
            pass
        return self.out