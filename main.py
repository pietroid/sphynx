from speechToText.audioCapture import AudioCapture
from speechToText.audioRecognition import AudioRecognition
from orchestrator.orchestrator import Orchestrator
import sounddevice as sd
import queue

samplerate = 44100
device = 18

audioCapture = AudioCapture(samplerate,device)
audioRecognition = AudioRecognition(samplerate)

orchestrator = Orchestrator()
orchestrator.setup()

with audioCapture.startCapture():
    print('capturing')
    while True:
        recognizedOutput = audioRecognition.recognize(audioCapture.audioOut)
        phrase = None
        try:
            phrase = recognizedOutput.get_nowait()
        except:
            pass
        if(phrase):
            print(phrase)
            orchestrator.putMessage({
                'type':'RAW',
                'content':phrase
            })
        orchestrator.runIteration()