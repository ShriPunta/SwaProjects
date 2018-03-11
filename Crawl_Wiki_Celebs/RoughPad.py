
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

import csv
header = []
fp= open(r"C:\Users\shrip\Pictures\url_downloads\crawler download\headers.csv", newline='')
reader = csv.reader(fp)
header = next(reader)
print(header)
fp.close()

import csv
with open(r"C:\Users\shrip\Pictures\url_downloads\crawler download\headers.csv", mode='r') as infile:
    reader = csv.reader(infile)
    for line in reader:
        print(line)

        for cell in line:
            print(line.index(cell))