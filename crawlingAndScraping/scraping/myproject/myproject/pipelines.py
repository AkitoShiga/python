# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from pymongo import MongoClient


class MyprojectPipeline:
    def process_item(self, item, spider):
        return item


class ValidationPipeline:

    """
    Itemを検証するPipeline
    """

    def process_item(self, item, spider):
        if not item['title']:
            # titleフィールドが取得できていない場合は破棄する
            # DropItem()の引数は破棄する理由を表すメッセージ
            raise DropItem('Missing title')


class MongoPipeline:

    """
    itemをmongodbに保存するpipeline
    """


    def open_spider(self, spider):
        """
        spiderの開始時にmongodbに接続する
        """
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['scraping-book']
        self.collection = self.db['items']


    def close_spider(self, item, spider):
        """
        itemをコレクションに追加する
        """
        # insert_one()の引数は書き換えられるので、コピーしたdictを渡す
        self.collection.insert_one(dict(item))
        return item



