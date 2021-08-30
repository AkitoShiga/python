import scrapy
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    # Spiderくんの名前
    name = 'news'

    # このドメインしかクロールしちゃだめ
    allowed_domains = ['news.yahoo.co.jp']

    # クロールの開始地点URL
    start_urls = ['https://news.yahoo.co.jp/']

    # 取得したWebページを処理するためのコールバック関数
    def parse(self, response):
        """
        トップページのトピックス一覧から個々のトピックスへのリンクを抜き出して表示する
        """
        
        # URLの配列が帰ってくる
        for url in response.css('div.contentsWrap a::attr("href")').re(r'/pickup/\d+$'):

            # 第一引数URL -> response
            # 第二引数 response に対するコールバック関数
            yield response.follow(url, self.parse_topics)


    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('title::text').get()
        item['body'] = response.css('p.highLightSearchTarget').xpath('string()').get()
        yield item
