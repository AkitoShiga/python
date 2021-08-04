import fileinput
with open('somefile3.txt') as f: # この時点ではイテラブルではない
    while True:
        char = f.read(1) # 一個ずつ読み出している
        print(char, end="")
        if not char:
            break

with open('somefile3.txt') as f:
    while True:
        char = f.readline(1)
        print(char, end="")
        if not char:
            break

with open('somefile3.txt') as f:
    for char in f.read(): # ここで文字列になってる
        print(char, end="")

print("\n---\n")
for line in fileinput.input('somefile3.txt'):
    print(line, end="")

print("\n---\n")

with open('somefile3.txt') as f: # ファイルオブジェクトは行ごとにイテレーションする
    for fs in f: # ここで文字列になってる
        print(fs)