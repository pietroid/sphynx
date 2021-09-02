from speechToText.audioCapture import AudioCapture
from speechToText.audioRecognition import AudioRecognition
from orchestrator.orchestrator import Orchestrator
from interpreter.interpreter import Interpreter
import sounddevice as sd
import queue

samplerate = 16000
device = 12

audioCapture = AudioCapture(samplerate,device)
audioRecognition = AudioRecognition(samplerate)

interpreter = Interpreter()

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