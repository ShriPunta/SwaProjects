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
        if not (isinstance(collectionToWrite, dict)):
            if isinstance(collectionToWrite, set):
                for item in collectionToWrite:
                    tempDict[item] = False

        tempList = list()
        for key,value in tempDict.items():
            tempDict2 = dict()
            tempDict2[key] = value
            tempList.append(tempDict2)

        con = Mong.ConnectToCloudDb()
        b = con.getDB(dbName='SwaProject')
        collec = con.getCollection(dbName='SwaProject', collecName='WikiCelebGraph')
        rec_id = collec.insert_one({'x': 55})



start_time = time.time()
testIntanst = CrawlerClass()
testIntanst.next_pages.append(r"/wiki/Category:American_male_film_actors")
testIntanst.theCrawler(base_url+testIntanst.next_pages[0])
print(len(testIntanst.to_crawl_sublinks))
testIntanst.writeMapToCSV(collectionToWrite=testIntanst.to_crawl_sublinks)
print("---%s seconds --"%(time.time() - start_time))
