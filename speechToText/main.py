import queue
import sounddevice as sd
import vosk

q = queue.Queue()

samplerate = 44100
device = 18
model = vosk.Model('stt_model_2')

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device, dtype='int16',
                            channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    print(rec.Result())