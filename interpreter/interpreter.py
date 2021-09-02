import spacy
from spacy.matcher import Matcher
import sys 

sys.path.append('../')
from utils.decorators import singleton

@singleton
class Interpreter:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = Matcher(self.nlp.vocab)
        self.match_n = 0
    
    def matches(self,text,pattern):
        self.matcher.add("match_n_"+str(match_n))
        self.match_n += 1
        doc = self.nlp(text)
        return self.matcher(doc)