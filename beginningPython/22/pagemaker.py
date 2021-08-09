from xml.sax.handler import ContentHandler
from xml.sax import parse

"""
TODO 下記の修正
1. if文制御
2. 閉じタグのハードコーディング
"""

class PageMaker(ContentHandler):

    # page要素を個別のファイルに切り出すためのフラグ
    # pageタグを検出したらTrue、終了タグを検知したらFalse
    passthrough = False

    # 開始タグの検知
    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            # 確かwモードはファイルが存在しなければ生成する
            self.out = open(attrs['name'] + '.html', 'w')
            self.out.write('<html>\n<head>\n<meta charset="UTF-8">\n')
            self.out.write('<title>{}</title>\n'.format(attrs['title']))
            self.out.write('</head>\n</body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            # itemsでタプルにしてる
            for key, val in attrs.items():
                self.out.write(' {} ="{}"'.format(key,val))
            self.out.write('>')

    # 閉じタグの検出、文字列は範囲外
    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body>\n</html>\n')
            self.out.close()

        # page内の要素の閉じタグをつける
        elif self.passthrough:
            #pass
            self.out.write('</{}>'.format(name))

    # pageタグ内の文字列を全部書き出す
    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)

parse('website.xml', PageMaker())
