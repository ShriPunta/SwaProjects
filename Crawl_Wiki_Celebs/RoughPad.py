
from pymongo import MongoClient


client = MongoClient("locahost",27017)
whichdb = "local"
db = client.whichdb
print(db)
whichCollection = "WikiCelebGraph"
wiki_collection = db.whichCollection
print(wiki_collection)
test_rec = [{"name" : "Test1",
            "traversed" : "Y",
            "gender" : "M",
            "age" : 10,
            }]
#rec_id = wiki_collection.insert_many(test_rec)
#print(rec_id)
#print(type(test_rec))
