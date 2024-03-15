from django.conf import settings
import pymongo

class WeatherRepository:

    colletion = ""
    def __init__(self) -> None:
        self.colletion = colletionName

    def getConnetion(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = pymongo.MongoClient(getattr(settings, "MONGO_DATABASE_NAME"))
   
   
    def getColletion(self):
        conn = self.getColletion()
        collection = conn[self.colletion]

        return collection
    
    def getAll(self):
        document= self.getColletion().find({})
        return object

    def insert(self, document):
        self.getColletion
        
