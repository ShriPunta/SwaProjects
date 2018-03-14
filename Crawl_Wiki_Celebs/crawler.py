import Crawl_Wiki_Celebs.mongoConnect as Mong
import Crawl_Wiki_Celebs.PlayDictAndCSV as DictCreator
import requests
from bs4 import BeautifulSoup
import time

base_url = r"https://en.wikipedia.org/wiki/"
crawler_mapper_csv_path = r""
start_page = r"https://en.wikipedia.org/wiki/Category:American_male_film_actors"


class CrawlerClass:
    to_crawl = set()
    crawled = set()

    if __name__ == '__main__':
        #Initialize the Mongo connect to WikiCeleb GRaph
        clie = Mong.MongoClient()
        to_crawl.add(start_page)



    def theCrawler(self,url_to_crawl):
        pass





    def getLinksToSpouses(self,subLink):
        source_code = requests.get(base_url+subLink)
        soup = BeautifulSoup(source_code.text, "lxml")
        soup2 = soup.find("div", {"class": "plainlist"})
        for a in soup2.find_all('a', href=True):
            self.to_crawl.add(a['href'])


