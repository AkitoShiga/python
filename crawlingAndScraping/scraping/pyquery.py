#!/Users/insightshiga/.pyenv/shims/python
from pyquery import PyQuery as pq

d = pq(filename='dp.html')
d.make_links_absolute('https//gihyo.jp/dp')

for a in d('#listbook > li > a[itemprop="url"]'):

    url = d(a).attr('href')
    p = d(a).find('p[itemporp="name"]').eq(0)
    title = p.text()
    print(url, title)
