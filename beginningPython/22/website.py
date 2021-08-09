
# ディスパッチャーミックスイン
class Dipatcher:
    """

    """
    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name,):
        self.dispatch('end', name)

    def dispatch(self, prefix, name, attrs=None):
      """
      必要なハンドラを探して引数を組み立てて投げる
      prefix -> start or end
      name -> elements
      attrs -> dict[attr, value]
      """

        # method name
        mname = prefix + name.capitalize()
        # default name
        dname = 'default' + prefix.capitalize()

        # メソッドを返す。getattrでメソッド返せるの？
        method = getattr(self, mname, None)

        # メソッドが実在したら空のタプルを作成
        if callable(method):
            args = ()
        else:
            method = getattr(self, dname, None)
            args = name, # タプルにしてる

        if prefix == 'start':
            args += attrs,

        if callable(method):
            method(*args)

# ヘッダー・フッターの処理
    def writeHeader(self, title):
        self.out.write("<html>\n <head>\n <title>")
        self.out.write(title)
        self.out.write("</title\n </head>\n <body>\n")

    def writeFooter(self):
        self.out.write("\n </body>\n</html>\n")

    def defaultStart(self, name, attrs):
        if self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' {}="{}"'.format(key,val))
            self.out.write('>')

    def defaultEnd(self, name):
        if self.passthrough:
            self.out.write('</{}>'.format(name))

class FileConstractor:
    def __init__(self, directory):
        self.directory = [directory]
        self.ensureDirectory()

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        os.makedirs(path, exist_ok=True)

    def startDirectory(self, attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()

    def endDirectory(self):
        self.directory.pop()

    def startPage(self, attrs):
        filename = os.path.join(*self.directory + [attrs['name'] + '.html'])
        self.out = open(filename, 'w')
        self.writeHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        self.passthrough = False
        self.writeFooter()
        self.out.close()