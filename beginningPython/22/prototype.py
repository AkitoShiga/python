from xml.sax.handler import  ContentHandler
from xml.sax import parse
"""
class TestHandler(ContentHandler):
    def startElement(self, name, attrs):
        print(name, attrs.keys());
    def endElement(self, name):
        print(name);

parse('website.xml', TestHandler())
"""

class HeadlineHandler(ContentHandler):

    in_headline = False

    def __init__(self, headlines):
        super().__init__()
        # H1要素を格納
        self.headlines = headlines
        self.data = []
    # フラグを立てて文字列を格納できる状態にする
    def startElement(self, name, attrs):
        print(self.data)
        if name == 'h1':
            self.in_headline =True

    # フラグが立っていたら格納してある文字列を静的な変数に格納
    def endElement(self, name):
        if name == 'h1':
            # ここの役割？
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    # 文字の検知して、フラグが立っていたら文字列を格納する
    def characters(self, string):
        if self.in_headline:
            self.data.append(string)

headlines = []
parse('website.xml', HeadlineHandler(headlines))

print('Found H1 elements')
for h in headlines:
    print(h)
