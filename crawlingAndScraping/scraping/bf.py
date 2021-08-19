#!/Users/insightshiga/.pyenv/shims/python

from bs4 import BeautifulSoup
with open('dp.html') as f:
    # インスタンスの生成はファイルオブジェクトで行うか、HTMLの文字列
    soup = BeautifulSoup(f, 'html.parser')
    '''
    # tagごと
    print(soup.title)
    # Tag
    print(type(soup.title))
    # BeautifulSoup
    print(type(soup))
    # タグ名
    print(soup.title.name)
    # タグの間の文字列
    print(soup.title.string)
    # NabigableString型
    # タグの中の要素に文字列とタグが混在している場合はNone
    print(type(soup.title.string))
    # Noneの場合はcnontentsで取得できる
    print(soup.title.contents)
    # stringじゃなくてtextなら混在してても行ける
    print(soup.title.text)
    # つなげて書けば行ける
    print(soup.title.p.string)
    # 基本的には最初にヒットしたやつだけっぽい
    print(soup.meta)
    # textで取得するとstrオブジェクトらしい
    print(type(soup.title.text))
    # タグ内の属性は辞書型で取得できる
    print(soup.h1['class'])
    '''
    # print(soup.find_all('meta'))
    print(soup.find_all('meta')[0])
    # 配列の中身はTagクラス。ちなみにResultSet型
    print(type(soup.find_all('meta')[0]))
    # 第2引数でタグの属性指定
    print(soup.find_all('meta', property='og:type'))
    # 属性だけで探すこともできる
    print(soup.find_all(property="og:type"))
    # BeutifulSoupは一部だけCSSセレクタが使える
    print(soup.select('li'))
