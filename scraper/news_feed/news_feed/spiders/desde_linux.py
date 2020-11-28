import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
from ..sumarize import sumarize
class desde_linux(scrapy.Spider):
    name = 'desde_linux'
    start_urls = ["https://blog.desdelinux.net/"]

    def parse(self,response):
        
        links=response.xpath("//h2[@class='post-title']/a/@href").getall()[:5]
        titles =response.xpath("//h2[@class='post-title']/a/text()").getall()[:5]
        i = 0
        for title in titles:
            link = links[i].lstrip()
            i = i + 1
            yield response.follow(url=link,callback=self.sumary,cb_kwargs={"title":title,"link":link})
            
    def sumary(self,response,**kwargs):
        items = TitularItem()
        items["link"] = kwargs["link"]
        items["title"] = kwargs["title"].lstrip()
        items["news_paper"] = "desde_linux"
        items["date"] = strftime("%Y-%m-%d",gmtime())
        _id = hashlib.md5(kwargs["title"].encode())
        items["_id"] = _id.hexdigest()
        text = response.xpath('//div[@class="post-content"]/p/text()').getall()
        if text == []:
            sumary = "no disponible"
        else:
            text = "".join(text)
            sumary = sumarize(text,"spanish")
        items["sumary"] = sumary
        yield items