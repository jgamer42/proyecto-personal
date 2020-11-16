import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
class desde_linux(scrapy.Spider):
    name = 'desde_linux'
    start_urls = ["https://www.welivesecurity.com/la-es/"]

    def parse(self,response):
        items = TitularItem()
        links=response.xpath("//h2[@class='post-title']/a/@href").getall()[:5]
        titles =response.xpath("//h2[@class='post-title']/a/text()").getall()[:5]
        i = 0
        for title in titles:
            items["link"] = links[i]
            items["title"] = title
            items["news_paper"] = "desde_linux"
            items["date"] = strftime("%Y-%m-%d",gmtime())
            _id = hashlib.md5(title.encode())
            items["_id"] = _id.hexdigest()
            i = i + 1
            yield items
 