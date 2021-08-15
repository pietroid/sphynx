import sys
sys.path.append('../../')
from orchestrator.orchestrator import Orchestrator

class WakeWord:
    def __init__(self):
        self.timeout = 10
        self.wakeWord = 'hey jarvis'
        self.orchestrator = Orchestrator()
        self.listeningKey = 'LISTENING'

    def apply(self,message):
        if(message['type'] == 'RAW'):
            contentText = message['content']['text']
            
            if(contentText.lower().find(self.wakeWord) >= 0):
                self.orchestrator.createMemory(self.listeningKey,None,self.timeout)
                newContentText = contentText.split(self.wakeWord)[-1]
                if(newContentText.strip() != ''):
                    outputMessage = message
                    outputMessage['content']['text'] = newContentText
                    #TODO: manipulate NLP to remove wakeWord from structure
                    return outputMessage
    
    def isListening(self):
        return len(self.orchestrator.listMemoriesByKey(self.listeningKey)) > 0