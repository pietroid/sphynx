import sys
import pkgutil
import inspect

sys.path.append('../')
from utils.decorators import singleton

import modules.custom as customModules
import modules.native as nativeModules

import datetime

def getModules(module):
    all_modules_classes = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            module.__path__, module.__name__ + '.'):
        _module = loader.find_module(module_name).load_module(module_name)
        for name,  obj in inspect.getmembers(_module):
            if(inspect.isclass(obj)):
                all_modules_classes.append(obj)
        print(all_modules_classes)
    return all_modules_classes
                

@singleton
class Orchestrator:
    def __init__(self):
        self.messages = []
        self.memories = [] #TODO: move to DB
    
    def setup(self):
        allModulesClasses = getModules(nativeModules) + getModules(customModules)
        self.modules = [obj() for obj in allModulesClasses] 

    def putMessage(self,message):
        self.messages.append(message)
    
    def getModules(self):
        return self.modules

    def createMemory(self,key,record,expirationInSeconds):
        created = datetime.datetime.now()
        expiration = created + datetime.timedelta(seconds = expirationInSeconds)
        self.memories.append({
            'key':key,
            'record':record,
            'created':created,
            'expiration':expiration
        })

    def listMemoriesByKey(self,key): # TODO: move to DB
        filtered = []
        now = datetime.datetime.now()
        for memory in self.memories:
            if(memory['key'] == key and now <= memory['expiration']):
                filtered.append(memory)
        return filtered

    def runIteration(self):
        outputMessages = []
        for message in self.messages:
            package = []
            for module in self.modules:
                output = module.apply(message)
                if(output is not None):
                    package.append(output)
            if(len(package) > 1):
                outputMessages.append({'type':'PACKAGE','content':package})
            elif(len(package) == 1):
                outputMessages.append(package[0])
        self.messages = outputMessages