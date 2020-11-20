import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
class desde_linux(scrapy.Spider):
    name = 'free_code_camp'
    start_urls = ["https://www.freecodecamp.org/news/"]

    def parse(self,response):
        items = TitularItem()
        links=response.xpath("//h2[@class='post-card-title']/a/@href").getall()[:5]
        titles =response.xpath("//h2[@class='post-card-title']/a/text()").getall()[:5]
        i = 0
        for title in titles:
            items["link"] = "https://www.freecodecamp.org/"+links[i].lstrip()
            items["title"] = title.lstrip()
            items["news_paper"] = "free_code_camp"
            items["date"] = strftime("%Y-%m-%d",gmtime())
            _id = hashlib.md5(title.encode())
            items["_id"] = _id.hexdigest()
            i = i + 1
            yield items