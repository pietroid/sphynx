import sys
sys.path.append('../')
from modules.templates import commandTemplate

class CustomModule(commandTemplate.CommandTemplate):

    def anticipate(self,message):
        contentText = message['content']['text']
            
        if(contentText.lower().find('hello') >= 0):
            newMessage = message
            newMessage['type'] = self.typeInputExecute
            return newMessage

    def execute(self,message):
        newMessage = message
        newMessage['type'] = self.typeOutputExecute
        print('HELLO! WHAT YOU WANT?')
        return newMessage