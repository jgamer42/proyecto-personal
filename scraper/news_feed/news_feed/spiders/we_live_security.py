import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
class desde_linux(scrapy.Spider):
    name = 'we_live_security'
    start_urls = ["https://www.welivesecurity.com/la-es/"]

    def parse(self,response):
        items = TitularItem()
        links = response.xpath("//article/a/@href").getall()
        titles = response.xpath("//article/a/div/div/h2/text()").getall()
        i = 0
        for title in titles:
            items["link"] = links[i]
            items["title"] = title
            items["news_paper"] = "we_live_security"
            items["date"] = strftime("%Y-%m-%d",gmtime())
            _id = hashlib.md5(title.encode())
            items["_id"] = _id.hexdigest()
            i = i + 1
            yield items

        