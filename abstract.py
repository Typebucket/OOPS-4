from abc import ABCMeta, abstractmethod
class parent(metaclass=ABCMeta):
    def printmsg(self, x):
        print("The parent value is: ", x)
    
    @abstractmethod
    def message(self):
        print("Im into the message method of the parent class")

class child(parent):
    def message(self):
        print("Im into the message method of the child class")

obj = child()
obj.message()
obj.printmsg(567)