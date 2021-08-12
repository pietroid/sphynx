from audio_capture import AudioCapture
from audio_recognition import AudioRecognition
import sounddevice as sd
import queue
samplerate = 44100
device = 18


audioCapture = AudioCapture(samplerate,device)
audioRecognition = AudioRecognition(samplerate)


with audioCapture.startCapture():
    while True:
        recognizedOutput = audioRecognition.recognize(audioCapture.audioOut)
        try:
            phrase = recognizedOutput.get_nowait()
            print(phrase)
        except:
            pass