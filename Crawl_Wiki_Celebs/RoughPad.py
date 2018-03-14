
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

from urllib3.util import parse_url
o = parse_url(r"http://www.cwi.nl:80/%7Eguido/Python.html")
for ele in o:
    print(ele)



import csv
mydict = {"a":"1","b":"2","c":"3","d":"4",}

filePathToWrite = r"C:\Users\shrip\Pictures\url_downloads\crawler download"
with open((filePathToWrite+'\\Traversed.csv'), 'w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
        writer.writerow([str(key), str(value)])


import requests
from bs4 import BeautifulSoup
import time

start_time= time.time()
source_code = requests.get(r"https://en.wikipedia.org/wiki/Category:American_male_film_actors")
soup = BeautifulSoup(source_code.text, "lxml")
for ul in soup.findAll("div", {"class": "mw-category-group"}):
    for li in ul.findAll('a'):
        print(li['href'])
print("---%s seconds --"%(time.time() - start_time))

for a in soup2.find_all('a', href=True):
    self.to_crawl.add(a['href'])