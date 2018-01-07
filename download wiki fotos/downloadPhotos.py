import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import random
base_dir = r'C:\\Users\\shrip\Pictures\\url_downloads\\crawler download\\'
url_to_crawl = "https://en.wikipedia.org/wiki/List_of_Bollywood_actresses/"

def image_ret(url):
    rand_name= random.randrange(0,100)
    #Using r transforms the string into a raw string
    #using double backslash treats 2nd backslash into a string instead
    #of recognizing it as \u or \r  special character

    full_name= base_dir + str(rand_name) +".jpeg"
    urllib.request.urlretrieve(url,full_name)

def crawler_method(url_to_crawl):
    domain = get_domain_name(url_to_crawl)
    i = 0

    source_code = requests.get(url_to_crawl)
    plain_text = source_code.text
    #print(plain_text)
    soup = BeautifulSoup(plain_text,"lxml")
    table = soup.find("td")
    #table2= soup.find("table").find_next_sibling("td").find("a")

    #print(table2)

    for classy in table.find("a": "href"):
        print(classy)
        continue
        if len(row) > 0:
            for cells in row.findAll("td"):
                if len(cells) > 0:
                    print(cells.text)


def get_domain_name(url):
    pattern = re.compile('^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?(?P<dom>[^:\/\n]+)')
    #print(pattern)
    #rand_name = random.randrange(0, 999999)
    matc = pattern.match(url)
    if matc is not None:
        dom = matc.groupdict()['dom']
        #print('Dom', dom)

    return dom[:-4]



crawler_method(url_to_crawl)