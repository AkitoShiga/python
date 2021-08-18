import re
from html import unescape
from urllib.parse import urljoin

with open('./dp.html') as f:
    html = f.read()

for partial_html in re.findall(
        r'<a itemprop="url" .*?</ul>\s*</a></li>', html, re.DOTALL):

    print(partial_html)
    print('=============================END============================')

    # 書籍のURLは itemprop="url" という属性を持つa要素のhref属性から取得する
    # タグ全体をマッチさせて()の中だけ取り出してる
    # 単独でマッチさせるのは無理っぽいけど要素とタグがわかれば行ける
    url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
    print(url)
    print('=============================END============================')
    # 絶対パス
    url = urljoin('https://gihyo.jp/', url)
    print(url)
    print('=============================END============================')

    # p要素全体の取得
    title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
    print(title)
    print('=============================END============================')

    title = title.replace('<br/>', ' ')
    print(title)
    print('=============================END============================')

    # テキストの部分は引っかからない
    title = re.sub(r'<.*?>', '', title)
    print(title)
    print('=============================END============================')
    # 文字参照を元に戻す
    title = unescape(title)
    break

    print(url, title)
