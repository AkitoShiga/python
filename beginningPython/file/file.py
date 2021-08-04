
# これでファイルオブジェクトが生成される、デフォルトは読み込みモード 'r'
#f = open('./hoi.txt')

f = open('somefile.txt', 'w')
# 自動で改行される訳ではない
print(f.write('Hello, \n')) #出力されるのは文字数
print(f.write('World!, \n'))
print(f.write('Konichiwa\n'))
print(f.write('皆さん!\n'))
f.close()

f = open('somefile.txt', 'r')
print(f.read(4))#引数に数値を渡すとその文字数読み込み
#途中から出力される。イテレーション？
print(f.read())
f.close()

