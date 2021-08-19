#! /Users/insightshiga/.pyenv/shims/python

from pyquery import PyQuery as pq

d = pq(filename='dp.html')
# PyQueryオブジェクト
print(type(d))
d = pq(url='http://example.com/')
d = pq("""
    <html>
    <head><title>八百屋オンライン</title></head>
""")
