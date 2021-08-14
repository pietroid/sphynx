import sys
import pkgutil
import inspect

sys.path.append('../')
from utils.decorators import singleton

import modules.custom as customModules
import modules.native as nativeModules

def getModules(module):
    all_modules_classes = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            module.__path__, module.__name__ + '.'):
        _module = loader.find_module(module_name).load_module(module_name)
        for name,  obj in inspect.getmembers(_module):
            if(inspect.isclass(obj)):
                all_modules_classes.append(obj)

    return all_modules_classes
                

@singleton
class Orchestrator:
    def __init__(self):
        self.messages = []
        self.memory = [] #TODO: move to DB
        allModulesClasses = getModules(nativeModules) + getModules(customModules)
        self.modules = [obj() for obj in allModulesClasses] 

    def putMessage(self,message):
        self.messages.append(message)
    
    def getModules(self):
        return self.modules

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