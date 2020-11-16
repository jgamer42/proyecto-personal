# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo 
class newsPipeline:
    def __init__(self):
        self.conection = pymongo.MongoClient("mongodb://localhost:27017")
        db = self.conection["proyecto_personal"]
        self.collection = db["titulares"]

    def process_item(self,item,spider):
        try:
            self.collection.insert(dict(item))
        except:
            print("titular repetido")
        return item
