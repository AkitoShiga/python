from scrapy.spiders import SitemapSpider

class IkeaSpder(SitemapSpider):
    """
    サイトマップを使用したクローリング
    """

    name = 'ikea'
    allowed_domains = ['www.ikea.com']

    # この設定がないと504エラーが発生することがあるらしい
    # settings.py で USER_AGENTを設定する場合は不要
    custom_settings = {
        'USER_AGENT' : 'ikeabot'
    }

    # XMLサイトマップのリスト
    # robots.txtのURLを指定すると、SitemapディレクティブからXMLサイトマップのURLを取得する
    sitemap_urls = [
        'https://www.ikea.com/robots.txt'
    ]

    # サイトマップインデックスからたどるサイトマップURLの正規表現のリスト
    # このリストの正規表現にマッチするURLのサイトマップのみをたどる
    sitemap_follow = [ r'prod-ja_JP' ]

    # サイトマップに含まれるURLを処理するコールバック関数を指定するルールのリスト
    # ルールは(正規表現、正規表現にマッチするURLを処理するコールバック関数)という2要素のタプルで指定する
    # sitemap_rulesを指定しない場合はすべてのURLのコールバック関数はparseメソッドとなる
    sitemap_rules = [
        (r'/products/', 'parse_product'),
    ]


    def parse_product(self, response):
        # 製品ページから製品の情報を抜き出す
        yield {
            'url'  : response.url,
            'name' : response.css('#name::text').get().strip(),
            'type' : response.css('#type::text').get().strip(),
            'price': response.css('#price1::text').re_first('[\S\xa0]+').replace('\xa0', ' '),
            # 価格 円記号と数値の間に\xa0が含まれているので、これをスペースに置き換える
        }
