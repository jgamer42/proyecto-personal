import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
from ..sumarize import sumarize
class real_python(scrapy.Spider):
    name = 'real_python'
    start_urls = [
        "https://realpython.com"
    ]

    def parse(self,response):
        
        main = self.main_article(response)
        others = self.other_articles(response)
        others.append(main)
        for article in others:
            yield response.follow(url=article["link"],callback=self.sumary,cb_kwargs = {'data':article})
            
    
    def main_article(self,response):
        article = {
            'link':self.start_urls[0]+response.xpath("//div[@class='card border-0']/div/a/@href").get(),
            'title':response.xpath("//div[@class='card border-0']/div/a/h2/text()").get(),
            'news_paper':'real python',
            'date':strftime("%Y-%m-%d",gmtime())
        }
       
        return article

    def other_articles(self,response):
        articles = []
        links = response.xpath("//div[@class='col-12 col-md-6 col-lg-4 mb-5']/div/div/a/@href").getall()[:4]
        titles = response.xpath("//div[@class='col-12 col-md-6 col-lg-4 mb-5']/div/div/a/h2/text()").getall()[:4]
        i = 0
        for title in titles:
            article={
                'link':self.start_urls[0] + links[i],
                'title':title,
                'news_paper':'real python',
                'date':strftime("%Y-%m-%d",gmtime())
            }
            i = i + 1
            articles.append(article)
        return articles
    
    def sumary(self,response,**kwargs):
        items = TitularItem()
        other_text = response.xpath('//div[@class="article-body"]/section[@class="section2"]/p/text()').getall()
        if other_text == []:
            sumary = "no disponible"
        else:
            other_text = "".join(other_text)
            sumary = sumarize(other_text,"english")
        items["link"] = kwargs["data"]["link"]
        items["title"] = kwargs["data"]["title"]
        items["news_paper"] = kwargs["data"]["news_paper"]
        items["date"] = kwargs["data"]["date"]
        _id = hashlib.md5(kwargs["data"]["title"].encode())
        items["_id"] = _id.hexdigest()
        items["sumary"]=sumary
        yield items
        