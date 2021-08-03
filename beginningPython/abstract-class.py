from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

#t = Talker()

class FrequentTalker(Talker):
    def talk(self):
        print("Hello")


t =  FrequentTalker()
t.talk()