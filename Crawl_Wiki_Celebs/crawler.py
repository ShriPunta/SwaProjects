import Crawl_Wiki_Celebs.mongoConnect as Mong
import Crawl_Wiki_Celebs.PlayDictAndCSV as DictCreator
import requests
from bs4 import BeautifulSoup

base_url = r"https://en.wikipedia.org/wiki/"
crawler_mapper_csv_path = r""
url_to_crawl = r"https://en.wikipedia.org/wiki/Robert_Downey_Jr."

class CrawlerClass:
    if __name__ == '__main__':
        #Initialize the Mongo connect to WikiCeleb GRaph
        clie = Mong.MongoClient()


    def theCrawler(self,url_to_crawl):

        all_links_found = set()





    def getLinksToSpouses(self,subLink):
        source_code = requests.get(url_to_crawl)
        soup = BeautifulSoup(source_code.text, "lxml")
        soup2 = soup.find("div", {"class": "plainlist"})
        for a in soup2.find_all('a', href=True):
            print(a['href'])

