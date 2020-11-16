# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TitularItem(scrapy.Item):
    date = scrapy.Field()
    news_paper = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    _id = scrapy.Field()