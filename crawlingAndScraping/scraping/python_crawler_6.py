#!/Users/insightshiga/.pyenv/shims/python

import re
import time
from typing import Iterator
import requests
import lxml.html
from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    collection = client.scraping.ebooks
    # インデックスの作成
    collection.create_index('key', unique=True)

    session = requests.Session()
    response = session.get('https://gihyo.jp/dp')

    # リストページからURLのリストを取得
    urls = scrape_list_page(response)

    for url in urls:
        # urlがDBに登録されているか確認して、なければ取得してDBに登録する
        key = extract_key(url)
        ebook = collection.find_one({'key': key})

        if not ebook:
            time.sleep(1)
            response = session.get(url)
            ebook = scrape_detail_page(response)
            collection.insert_one(ebook)

        print(ebook)


def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """
    詳細ページのURLリストを抜き出す
    """
    html = lxml.html.fromstring(response.text)
    # これはすべての項目に対してやってるっぽい
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        print(url)
        yield url


def scrape_detail_page(response: requests.Response):
    """
    詳細ページのResponseから電子書籍の情報をdictで取得する
    """
    html = lxml.html.fromstring(response.text)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': html.cssselect('#bookTitle')[0].text_content(),
        'price': html.cssselect('.buy')[0].text.strip(),
        'content': [normalize_spaces(h3.text_content()) for h3 in html.cssselect('#content > h3')]
    }

    return ebook


def extract_key(url: str) -> str:
    """
    URL からキー（末尾のISBN）を抜き出す
    """
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)


def normalize_spaces(s: str) -> str:
    """
    改行文字と空白文字の削除
    """
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()
