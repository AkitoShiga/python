# /Users/insightshiga/Documents/sandbox/python/crawlingAndScraping/scraping/bin/python
import lxml.html

# HTMLファイルを読み込み、getroot()メソッドでHtmlElementオブジェクトを得る
tree = lxml.html.parse('dp.html')
html = tree.getroot()
# 引数のURLを基準として、すべてのa要素のhref属性を絶対URLに変換する
html.make_links_absolute('https://gihyo.jp/')

# cssselect()メソッドで、セレクターに該当するa要素のリストを取得して、個々のa要素に対して処理を行う
# セレクターの意味:id="listbook"である要素の子であるli要素の子であるitemprop="url"という属性を持つa要素
for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    # a要素のhref属性から書籍のURLを取得する
    url = a.get('href')
    # 書籍のタイトルはitemprop="name"という属性を持つp要素から取得する
    p = a.cssselect('p[itemprop="name"]')[0]
    title = p.text_content()
    print(url, title)
