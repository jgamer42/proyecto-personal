import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
class desde_linux(scrapy.Spider):
    name = 'hacks4all'
    start_urls = ["https://haxf4rall.com/"]

    def parse(self,response):
        items = TitularItem()
        links=response.xpath('//div[@class="banner-header"]/h3/a/@href').getall()[:5]
        titles =response.xpath('//div[@class="banner-header"]/h3/a/text()').getall()[:5]
        i = 0
        for title in titles:
            items["link"] = links[i].lstrip()
            items["title"] = title.lstrip()
            items["news_paper"] = "hacks4all"
            items["date"] = strftime("%Y-%m-%d",gmtime())
            _id = hashlib.md5(title.encode())
            items["_id"] = _id.hexdigest()
            i = i + 1
            yield items
 