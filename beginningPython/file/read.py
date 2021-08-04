import pprint
f = open('somefile.txt')

print('---read---')
print(f.read(7)) # First l
print(f.read(4)) # ine
print(f.read()) # のこり
f.close()

print('---readline---')
f = open('somefile.txt')
for i in range(4):
    print(str(i) + ': ' + f.readline() , end='') # end=''を引数に指定しないと改行コードが二重で出力される
print()
f.close()

print('---readlines---')
pprint.pprint(open('somefile.txt').readlines())
print(open('somefile.txt').readlines()) # 出力結果は上と変わらない