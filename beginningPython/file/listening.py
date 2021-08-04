#!/Users/insightshiga/.pyenv/shims/python
import sys #標準入力を使用するためのモジュール
# 標準入力の読み込み、出力を行う


text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('単語数:', wordcount)

