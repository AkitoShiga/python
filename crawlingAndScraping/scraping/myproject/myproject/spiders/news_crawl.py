from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myproject.items import Headline

class NewsSpider(CrawlSpider):

    name = 'news_crawl'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    # リンクをたどるルール
    rules = {
                # トピックスのページのリンクをたどり、レスポンスをparse_topics()メソッドで処理する。
                # 複数のルールを指定して、それぞれのコールバックで実行することも可能
                Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics')
            }


    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('title::text').get()
        item['body'] = response.css('p.highLightSearchTarget').xpath('string()').get()
        yield item
