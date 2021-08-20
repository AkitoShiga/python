#! /Users/insightshiga/.pyenv/shims/python

from pyquery import PyQuery as pq

d = pq(filename='dp.html')
# PyQueryオブジェクト
print(type(d))
d = pq(url='http://example.com/')

d = pq("""
    <html>
    <head><title>八百屋オンライン</title></head>
    <body>
    <h1 id="main"><strong>おいしい</strong>今日のくだもの</h1>
    <ul>
        <li>りんご</li>
        <li class="featured">みかん</li>
        <li>ぶどう</li>
    </ul>
    </body>
    </html>
""")
'''
print(d('h1'))
print(type(d('h1')))
print(d('h1')[0])
print(d('h1').text())
print(d('h1').attr.id)
print(d('h1').attr['id'])
'''

# print(d('h1').children())
print(d('h1').parent())
