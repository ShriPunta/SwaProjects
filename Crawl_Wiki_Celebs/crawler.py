import Crawl_Wiki_Celebs.mongoConnect as Mong
import Crawl_Wiki_Celebs.PlayDictAndCSV as DictCreator
import requests
from bs4 import BeautifulSoup

base_url = r"https://en.wikipedia.org/wiki/"
crawler_mapper_csv_path = r""
start_page = r"https://en.wikipedia.org/wiki/Robert_Downey_Jr."


class CrawlerClass:
    all_links_found = set()
    to_crawl = [start_page]

    if __name__ == '__main__':
        #Initialize the Mongo connect to WikiCeleb GRaph
        clie = Mong.MongoClient()


    def theCrawler(self,url_to_crawl):
        for k in range(0, 3):
            i = 0  # Initiate Variable to count No. of Iterations
            while i < 3:
                urll = self.to_crawl.pop(0)



    def getLinksToSpouses(self,subLink):
        source_code = requests.get(url_to_crawl)
        soup = BeautifulSoup(source_code.text, "lxml")
        soup2 = soup.find("div", {"class": "plainlist"})
        for a in soup2.find_all('a', href=True):
            self.all_links_found.add(a['href'])

