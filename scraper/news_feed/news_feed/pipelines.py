# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
import pymongo 
class newsPipeline:
    def __init__(self):
        uri = os.getenv("DB_URI")
        self.conection = pymongo.MongoClient(uri)
        db = self.conection["proyecto"]
        self.collection = db["titulares"]

    def process_item(self,item,spider):
        try:
            self.collection.insert(dict(item))
        except:
            print("titular repetido")
        return item
