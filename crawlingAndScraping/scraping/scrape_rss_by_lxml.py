#!/Users/insightshiga/.pyenv/shims/python

import lxml.etree

# parse関数でファイルを読み込んでElementTreeオブジェクトを得る
tree = lxml.etree.parse('rss2.xml')
# getrootでXMLのルート要素に対応するElementオブジェクトを取得
root = tree.getroot()
print(root)

for item in root.findall('channel/item'):
    title = item.find('title').text
    url = item.find('link').text
    print(url, title)
