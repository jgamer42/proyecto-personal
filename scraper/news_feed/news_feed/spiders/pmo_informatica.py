import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
class desde_linux(scrapy.Spider):
    name = 'pmo_informatica'
    start_urls = ["http://www.pmoinformatica.com/"]

    def parse(self,response):
        items = TitularItem()
        links=response.xpath("//h3[@class='post-title entry-title']/a/@href").getall()[:5]
        titles =response.xpath("//h3[@class='post-title entry-title']/a/text()").getall()[:5]
        i = 0
        for title in titles:
            items["link"] = links[i].lstrip()
            items["title"] = title.lstrip()
            items["news_paper"] = "pmo_informatica"
            items["date"] = strftime("%Y-%m-%d",gmtime())
            _id = hashlib.md5(title.encode())
            items["_id"] = _id.hexdigest()
            i = i + 1
            yield items