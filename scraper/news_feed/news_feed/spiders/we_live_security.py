import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
from ..sumarize import sumarize
class desde_linux(scrapy.Spider):
    name = 'we_live_security'
    start_urls = ["https://www.welivesecurity.com/la-es/"]

    def parse(self,response):
        items = TitularItem()
        links = response.xpath("//article/a/@href").getall()
        titles = response.xpath("//article/a/div/div/h2/text()").getall()
        i = 0
        for title in titles:
            link = links[i].lstrip()
            i = i + 1
            yield response.follow(url=link,callback=self.sumararizer,cb_kwargs={"title":title,"link":link})
    
    def sumararizer(self,response,**kwargs):
        items = TitularItem()
        text = response.xpath('//div[@class="col-md-10 col-sm-10 col-xs-12 formatted"]/p/text()').getall()
        if text == []:
            sumary="no disponible"
        else:
            text = "".join(text)
            sumary = sumarize(text,"spanish")
        items["link"] = kwargs["link"]
        items["title"] = kwargs["title"].lstrip()
        items["news_paper"] = "we_live_security"
        items["date"] = strftime("%Y-%m-%d",gmtime())
        _id = hashlib.md5(kwargs["title"].encode())
        items["_id"] = _id.hexdigest()
        items["sumary"] = sumary
        yield items
         

        