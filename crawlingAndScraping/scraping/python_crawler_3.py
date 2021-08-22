#!/Users/insightshiga/.pyenv/shims/python

from typing import Iterator
from pymongo import MongoClient
import time
import requests
import lxml.html


def main():

    # 複数のページをクロールする際はSessisonを使う
    session = requests.Session()
    responseList = requests.get('https://gihyo.jp/dp')
    urls = scrape_list_page(responseList)

    # db
    client = MongoClient('localhost', 27017)
    db = client.scraping
    collection = db.books
    collection.delete_many({})

    for url in urls:
        time.sleep(1)
        # sessionを使って詳細ページを取得
        responseDetail = session.get(url)

        ebook = scrape_detail_page(responseDetail)
        collection.insert_one(ebook)

        print(ebook)


# リストページからURLの抜き出し
def scrape_list_page(responseList: requests.Response) -> Iterator[str]:
    html = lxml.html.fromstring(responseList.text)
    html.make_links_absolute(responseList.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        yield url


def scrape_detail_page(responseDetail: requests.Response) -> dict:
    html = lxml.html.fromstring(responseDetail.text)
    ebook = {
        'url': responseDetail.url,
        'title': html.cssselect('#bookTitle')[0].text,
        'price': html.cssselect('.buy')[0].text.strip(),
        'content': [h3.text_content() for h3 in html.cssselect('#content > h3')],
    }
    return ebook


if __name__ == '__main__':
    main()
