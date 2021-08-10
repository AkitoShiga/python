from xml.sax.handler import  ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):
    def startHandler(self, name, attrs):
        print(name, attrs.keys())
parse('website.xml', TestHandler())

'''
1. 要素の始まり（タグの検出）
2. 要素の終了（終了タグの検出）
3. プレーンテキスト
'''

