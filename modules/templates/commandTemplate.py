import sys
sys.path.append('../')
from modules.native.wakeWord import WakeWord

class CommandTemplate:
    def __init__(self):
        self.typeInputAnticipate = 'RAW'
        self.typeInputExecute = 'READY'
        self.typeOutputAnticipate = 'PREPARING'
        self.typeOutputExecute = 'DONE'


    def anticipate(self,message):
        pass

    def execute(self,message):
        pass

    def apply(self,message):
        if(message['type'] == self.typeInputAnticipate):
            if(WakeWord().isListening()):
                return self.anticipate(message)
        
        elif(message['type'] == self.typeInputExecute):
            return self.execute(message)
