
from pymongo import MongoClient
import dns

class ConnectToCloudDb:
    client = None
    db = None
    collec = None
    last_inserted_recIds = None

    def __init__(self,dbName,collecName):
       #client = MongoClient("mongodb://shri_punta:Shridhar28@cluster0-shard-00-00-vpcnk.mongodb.net:27017,cluster0-shard-00-01-vpcnk.mongodb.net:27017,cluster0-shard-00-02-vpcnk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
       self.client = MongoClient("mongodb+srv://shri_punta:Shridhar28@cluster0-vpcnk.mongodb.net/test")
       self.db = self.client[dbName]
       self.collec = self.db[collecName]

    def getDB(self,dbName):
        self.db = self.client[dbName]
        return self.db

    def getCollection(self,dbName,collecName):
        db = self.client[dbName]
        self.collec = db[collecName]
        return self.collec

    def insertManyWiki(self,dataToInsertMap):
        self.last_inserted_recIds = self.collec.insert(dataToInsertMap,check_keys=False)
        return self.last_inserted_recIds

    def deleteAll(self):

        rec_id = self.collec.delete_many({})




'''con = ConnectToCloudDb()



db = con.getDB(dbName='SwaProject')
collec = con.getCollection(dbName='SwaProject',collecName='WikiCelebGraph')
rec_id = collec.insert_one({'x':55})
print(rec_id)'''
