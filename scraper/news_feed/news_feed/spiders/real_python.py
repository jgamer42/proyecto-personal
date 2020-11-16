import scrapy
from time import strftime , gmtime
import hashlib
from ..items import TitularItem
class real_python(scrapy.Spider):
    name = 'real_python'
    start_urls = [
        "https://realpython.com/"
    ]

    def parse(self,response):
        items = TitularItem()
        main = self.main_article(response)
        others = self.other_articles(response)
        others.append(main)
        i = 0
        for article in others:
            items["link"] = article["link"]
            items["title"] = article["title"]
            items["news_paper"] = article["news_paper"]
            items["date"] = article["date"]
            _id = hashlib.md5(article["title"].encode())
            items["_id"] = _id.hexdigest()
            i = i + 1
            yield items
    
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