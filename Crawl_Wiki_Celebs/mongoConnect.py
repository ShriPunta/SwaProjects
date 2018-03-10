
from pymongo import MongoClient


class ConnectToLocalDb:
    client = None
    db = None
    wiki_collection = None
    last_inserted_recIds = None

    def __init__(self,hostName='localhost',port=27017):
       self.client = MongoClient(hostName,port)
       return self.client

    def getDB(self,dbName):
        self.db = self.client.local
        return self.db

    def getCollection(self,collectionName):
        self.wiki_collection = self.db.WikiCelebGraph
        return self.wiki_collection

    def insertManyWiki(self,dataToInsertMap):
        self.last_inserted_recIds = self.wiki_collection.insert_many(dataToInsertMap)
        return self.last_inserted_recIds





