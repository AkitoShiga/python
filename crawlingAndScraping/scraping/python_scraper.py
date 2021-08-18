#!/Users/insightshiga/Documents/sandbox/python/crawlingAndScraping/scraping/bin/python

from typing import List
import csv
import requests
import lxml.html

def main():

    url = 'https://gihyo.jp/dp'
    file = '/Users/insightshiga/Documents/sandbox/python/crawlingAndScraping/scraping/books.csv'

    html = fetch(url)
    books = scrape(html, url)
    save(file, books)


def fetch(url: str) -> str:

    r = requests.get(url)
    r = r.text
    print(r)
    return r


def scrape(html: str, base_url: str) -> List[dict]:

    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):

        url = a.get('href')
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content()

        books.append({'url': url, 'title': title})

    return books


def save(file_path: str, books: List[dict]):
    with open(file_path, 'w', newline='') as f:

        writer = csv.DictWriter(f, ['url', 'title'])
        writer.writeheader()
        writer.writerows(books)

    for li in books:
        print(li)


if __name__ == '__main__':
    main()
