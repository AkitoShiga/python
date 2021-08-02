
'''
girls = ['かなこ','ゆう','ひでみ']
boys = ['ゆうへい', 'ひろし', 'かずき']

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)

print(letterGirls)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])

def print_params_2(title, *params):
    print(title)
    print(params)

print_params_2('args', 1, 2, 3)
print_params_2('args')

def in_the_middle(x, *y, z):
    print(x,y,z)

in_the_middle(1,2,3,4,5, z=6)
#in_the_middle(1,2,3,4,5, 6)

def in_the_middle2(**params):
    print(params)

in_the_middle2(foo=100, bar=100)

args = {'name': 'Taro', 'age': 42}
hoi = [1,2,3]
def with_stars(name, age):
    #print(f"{kwds['name']}, is {kwds['age']} desu")
    print(f"{name}, is {age} desu")

with_stars(**args)

def without_stars(kwds):
    print(f"{kwds['name']}, is {kwds['age']} desu")
without_stars(args)

def hei(x,y,z):
    print(str(x + y + z))
hei(*hoi)
'''

def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor

double = multiplier(2)
print(str(double(5)))
print(multiplier(2)(5))

