import scrapy

from myproject.items import Page
from myproject.utils import get_content

class BroadSpder(scrapy.Spider):
    name = 'broad'
    # はてなブックマークの新着ページエントリー
    start_urls = ['https://b.hatena.ne.jp/entrylist/all']


    def parse(self, response):
        """
        はてなブックマークの新着ページエントリーをパースする
        """
        # 個別のWebページへのリンクをたどる
        for url in response.css('.entrylist-contents-title > a::attr("href")').getall():
            # parse_pageをコールバックとして利用
            yield scrapy.Request(url, callback=self.parse_page)

        # page=値が一桁である間のみ「次の20件」のリンクをたどる（最大9ページまで）
        url_more = response.css('.entrylist-readmore > a::attr("href")').re_first(r'.*\?page=\d{1}$')
        if url_more:
            yield response.follow(url_more)


    def parse_page(self, response):
        """
        個別のWebページをパースする
        """
        # utils.pyに定義したget_content()関数でタイトルと本文を抽出する
        title, content = get_content(response.text)
        # Pageオブジェクトを作成してyieldする
        yield Page(url=response.url, title=title, content=content)
