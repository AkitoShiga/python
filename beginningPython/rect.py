"""
class Rectangle:
    def __init__(self):
        self.width  = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size) #これを宣言することで内部的にいろんな関数が動く様になるらしい
    #setter, getter を sizeにバインドすることで、メンバ変数の様に使える


r = Rectangle()
r.width  = 10
r.height = 5

print(r.get_size())
r.set_size((150, 100))

print(r.width)

print(r.size)
#タプル形式じゃなくてもいける？
r.size = 999, 999
print(r.size)
"""

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

r = Rectangle()
r.size = 100, 200
print(r.size)
