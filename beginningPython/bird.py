
class Bird():
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('eat')
            self.hungry = False
        else:
            print('full')

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'HOOOOOOO'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()