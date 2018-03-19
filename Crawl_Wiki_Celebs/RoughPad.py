
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
'''for ul in soup.findAll("div", {"class": "mw-category-group"}):
    for li in ul.findAll('a'):
        print(li['href'])'''

print("---%s seconds --"%(time.time() - start_time))

for divs in soup.findAll('a',text="next page"):
    print(divs['href'])

print("---%s seconds --"%(time.time() - start_time))

for a in soup2.find_all('a', href=True):
    self.to_crawl.add(a['href'])




mylist = [4, 2, 8, 4, 9, 6, 7]
N = 3
cumsum, moving_aves = [0], []

for i, x in enumerate(mylist, 1):
    cumsum.append(cumsum[i-1] + x)
    print("i = ",i," x= ",x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        print('Single ---> ',moving_ave)
        moving_aves.append(moving_ave)
print("All--> ",moving_aves)


# Complete the function below.

inputs = [1, 2, 100, 2, 2]
allowedIncrease = 2.5
windowSize = 2
total_avg = sum(inputs) / len(inputs)
threshold = int(allowedIncrease) * total_avg
flag = 0
N = int(windowSize)
cumsum, all_aves = [0], []
for i, x in enumerate(inputs, 1):
    cumsum.append(cumsum[i - 1] + x)
    print("i = ", i, " x= ", x)
    if i >= N:
        moving_ave = (cumsum[i] - cumsum[i - N]) / N
        print('Single ---> ', moving_ave)
        if moving_ave < threshold:
            flag = 2

        if len(all_aves)>0 and (moving_ave > ((all_aves[-1]) * int(allowedIncrease))):
            flag = 1
            print("True")
            break

        all_aves.append(moving_ave)
print("All--> ", all_aves)
if flag == 2:
    print("False")

from bs4 import BeautifulSoup

soup = BeautifulSoup(source_code.text, "lxml")
for ul in soup.findAll("div", {"class": "mw-category-group"}):
    print("Entered Ul")
    for li in ul.findAll('a', href=True):
        print(li['href'])
        self.to_crawl_sublinks.add(li['href'])







