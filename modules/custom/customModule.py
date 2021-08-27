import sys
sys.path.append('../')
from modules.templates import commandTemplate
from services import textToSpeech

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
        tts = textToSpeech.TextToSpeech()
        tts.speak('Hello!! How are you doing? Are you alright?')
        return newMessage