#!/Users/insightshiga/.pyenv/shims/python

import lxml.html
from pymongo import MongoClient

# DB接続
client = MongoClient('localhost', 27017)

# スキーマ作成
db = client.scraping

# コレクション作成
collection = db.books
collection.delete_many({})

tree = lxml.html.parse('dp.html')
html = tree.getroot()
html.make_links_absolute('https://gihyo.jp/')
for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
    url = a.get('href')
    p = a.cssselect('p[itemprop="name"]')[0]
    title = p.text_content()
    collection.insert_one({'url': url, 'title': title})

for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])
