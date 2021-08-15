import sounddevice as sd
import queue
import sys

class AudioCapture:
    def __init__(self,samplerate,device):
        self.audioOut = queue.Queue()
        self.samplerate = samplerate
        self.device = device

    def _callback(self,indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.audioOut.put(bytes(indata))

    def startCapture(self): 
        return sd.RawInputStream(samplerate=self.samplerate, blocksize = 8000, device=self.device, dtype='int16',channels=1, callback=self._callback)