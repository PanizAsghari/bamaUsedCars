from bs4 import BeautifulSoup
from dataExtraction.management import open_page
import unicodedata

#main defs for data extractions

def extract_url_info(url):
    url_segments=url.split('/')
    for segment in url_segments:
        if "details" in segment:
            seg_id=segment
    print(seg_id)
    print(url)

def make_soup(page):
    page = BeautifulSoup(page , "lxml")
    return page


def extract_info(page):
   #finding main attributes from car pages
    info = page.find("div", {"class":"inforight"})
    attributes = info.find_all('span',{'class':False})
    release_date= attributes[0].get_text()
    brand = attributes[1].get_text()
    model = attributes[2].get_text()
    price = attributes[5].get_text()
    mileage = attributes[7].get_text()
    gear = attributes[8].get_text()
    fuel = attributes[9].get_text()
    body_status = attributes[10].get_text()
    color = attributes[11].get_text()
    state = attributes[12].get_text()

   # finding user defined description for furthur studies
    info = page.find('span',{'itemprop':'description'} )



    description = info.get_text()
    print(description)
    print(mileage)
    print(price)
    print(release_date)
    print(brand)
    print(model)
    print(gear)
    print(fuel)
    print(body_status)
    print(color)
    print(state)

def extractor(url):
    page=open_page(url)
    data=make_soup(page)
    extract_info(data)
