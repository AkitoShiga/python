#!/Users/insightshiga/.pyenv/shims/python
f = open('somefile2.txt', 'w')
print(f.write('this\nis no\nhaiku\n'))
print(f.write('これは\n俳句では\nありません'))
f.close()

f = open('somefile2.txt')
lines = f.readlines() # テキストファイルをコレクションにして変数に代入
f.close()
lines[1] = "isn't a\n"
f = open('somefile3.txt', 'w')
f.writelines(lines)
f.close()