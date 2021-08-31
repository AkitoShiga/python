import os
from urllib.parse import urlencode
import scrapy

class FlickrSpider(scrapy.Spider):
    name = 'flickr'
    # Files Pipelineでダウンロードされる画像ファイルはallowed_domainsに
    # 制限されないのでallowed_domains に'staticflicker'を追加する必要はない
    allowed_domains = ['api.flickr.com']


    # キーワード引数でSpider引数の値を受ける
    def __init__(self, text='sushi'):
        super().__init__() # 親クラスの__init__()を実行

        # 環境変数とSpider引数の値を使ってstarts_urlを組み立てる
        # urlencode()関数は引数に指定したdictのキーと値をURLエンコードして
        # key1=value1&key2=value2という形式の文字列を返す
        self.start_urls = [
            enco = dict()
            enco = {
                'method'  : 'flickr.photos.search',
                'api_key' : '',
                'text'    : text,
                'sort'    : 'relevance',
                'license' : '4,5,9'
            }

            'https://api.flickr.com/services/rest/?' + urlencode(enco),
        ]

    def parse(self, response):
        """
        APIのレスポンスをパースしてfile_urlsというキーを含むdictをyieldする
        """
        for photo in response.css('photos'):
            yield{'file_urls': [flickr_photo_url(photo)]}


def flickr_photo_url(photo: scrapy.Selector) -> str:
    """
    Flickrの写真を組み立てる
    """
    attrib = dict()
    attrib = dict(photo.attrib)
    attrib['size'] = 'b'
    return 'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}_{size}.jpg'.format(**attrib)



