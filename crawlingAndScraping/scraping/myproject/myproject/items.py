# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Headline(scrapy.Item):
    """
    ニュースのヘッドラインを表す Item
    定義した値以外を入れると例外がスローされる
    """
    title = scrapy.Field()
    body  = scrapy.Field()



class Restaurant(scrapy.Item):
    name      = scrapy.Field()
    address   = scrapy.Field()
    latitude  = scrapy.Field()
    longitude = scrapy.Field()
    station   = scrapy.Field()
    score     = scrapy.Field()
