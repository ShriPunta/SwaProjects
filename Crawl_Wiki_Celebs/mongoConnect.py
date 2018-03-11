
from pymongo import MongoClient


class ConnectToLocalDb:
    client = None
    db = None
    wiki_collection = None
    last_inserted_recIds = None

    def __init__(self,hostname='localhost',port=27017):
       self.client = MongoClient(hostname,port)
       self.db = self.client.local
       self.wiki_collection = self.db.WikiCelebGraph

    def getDB(self):
        return self.db

    def getCollection(self):
        return self.wiki_collection

    def insertManyWiki(self,dataToInsertMap):
        self.last_inserted_recIds = self.wiki_collection.insert_many(dataToInsertMap)
        return self.last_inserted_recIds





