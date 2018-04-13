import Crawl_Wiki_Celebs.mongoConnect as Mong
#import Crawl_Wiki_Celebs.PlayDictAndCSV as DictCreator
import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = r"https://en.wikipedia.org"
crawler_mapper_csv_path = r""
start_page = r"https://en.wikipedia.org/wiki/Category:American_male_film_actors"


class CrawlerClass:
    to_crawl_sublinks = set()
    crawled = set()
    next_pages = list()
    con = None
    find_spouses = set()

    def __init__(self):
        pass

    def main(self):
        pass
        # Initialize the Mongo connect to WikiCeleb GRaph
        #clie = Mong.MongoClient()
        #self.next_pages.append(r"/wiki/Category:American_male_film_actors")



    def theCrawler(self,url_to_crawl):
        i=0
        while i<1 and len(self.next_pages) != 0:
            print("Entered" ,i)
            #print("Crawling Links -->",self.to_crawl_sublinks)
            #print("Next Pages -->",self.next_pages)

            if len(self.next_pages) != 0:
                nowLink = self.next_pages.pop(0)
                #print(nowLink)
            else:
                break
            self.getNamesOfAllActors(nowLink)
            self.crawled.add(nowLink)
            i += 1

    def getTheNextPageLink(self,soup):
        #print("Get Next Page -->")
        try:
            for divs in soup.findAll('a', text="next page"):
                print(divs['href'])
                self.next_pages.append(divs['href'])
                break

        except:
            print("Did not find next page")
        #print("next pages -->",self.next_pages)


    def getNamesOfAllActors(self,sublinkToCrawl):
        print("page being acccessed ==>",base_url+sublinkToCrawl)
        source_code = requests.get(base_url+sublinkToCrawl)
        #print(len(source_code.text))
        soup = BeautifulSoup(source_code.text, "lxml")
        for ul in soup.findAll("div", {"class": "mw-category-group"}):
            #print("Entered Ul")
            for li in ul.findAll('a', href=True):
                #print(li['href'])
                self.to_crawl_sublinks.add(li['href'])
        self.getTheNextPageLink(soup)

    def getLinksToSpouses(self,subLink):
        print(base_url+subLink)
        source_code = requests.get(base_url+subLink)
        soup = BeautifulSoup(source_code.text, "lxml")
        soup2 = soup.find("div", {"class": "plainlist"})
        for a in soup2.find_all('a', href=True):
            self.to_crawl_sublinks.add(a['href'])

    def writeMapToCSV(self,collectionToWrite,writeCollecToCSVpath=r"C:\Users\shrip\Pictures\url_downloads\crawler download"):
        tempDict = dict()
        # print(type(collectionToWrite))
        # print(isinstance(collectionToWrite,dict))
        if not (isinstance(collectionToWrite, dict)):
            if isinstance(collectionToWrite, set):
                for item in collectionToWrite:
                    tempDict[item] = False
        #filePathToWrite = r"C:\Users\shrip\Pictures\url_downloads\crawler download" if writeMapToCSVpath!=('' or None) else writeMapToCSVpath
        with open((writeCollecToCSVpath + '\\Traversed4.csv'), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in tempDict.items():
                writer.writerow([str(key), str(value)])

    def writeToMongoDB(self,collectionToWrite):
        tempDict = dict()
        tempList = list()

        if not (isinstance(collectionToWrite, dict)):
            if isinstance(collectionToWrite, set):
                for item in collectionToWrite:
                    tempDict['sublink'] = item
                    tempDict['traversed'] = False
                    tempList.append(tempDict)


        if self.con==None:
            self.con = Mong.ConnectToCloudDb(dbName='SwaProject',collecName='WikiCelebGraph')
        rec_ids = self.con.insertManyWiki(tempList)


start_time = time.time()
testIntanst = CrawlerClass()
#testIntanst.next_pages.append(r"/wiki/Category:American_male_film_actors")
#testIntanst.theCrawler(base_url+testIntanst.next_pages[0])
#print(len(testIntanst.to_crawl_sublinks))
##testIntanst.writeMapToCSV(collectionToWrite=testIntanst.to_crawl_sublinks)
#testIntanst.writeToMongoDB(testIntanst.to_crawl_sublinks)
#rec_id = testIntanst.con.deleteAll()
plon=Mong.ConnectToCloudDb(dbName='SwaProject',collecName='WikiCelebGraph')
#plon.deleteAll()
# Create text index

#plon.collec.create_index([('sublink',pymongo.TEXT)])

# Text search
cli = None
for ele in list(plon.collec.find({}).limit(10)):
    testIntanst.to_crawl_sublinks.add(ele['sublink'].replace('??','.'))

i=1
while(len(testIntanst.to_crawl_sublinks) !=0):
    #print(testIntanst.to_crawl_sublinks)

    print(' i = ',i)
    toPop = base_url+'/wiki/' + testIntanst.to_crawl_sublinks.pop()
    source_code = requests.get(toPop)
    soup = BeautifulSoup(source_code.text, "lxml")
    soup2 = soup.find_all(text="Spouse")
    if soup2 != None:
        for a in soup2:
            print(a)

    i+=1

#for ele in plon.collec.find({"sublink":{"$regex" : "*._*"}}).limit(4):
#    print("Val ==> ",ele)
print("---%s seconds --"%(time.time() - start_time))
