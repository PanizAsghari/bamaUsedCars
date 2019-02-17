from bs4 import BeautifulSoup
from dataExtraction.management import open_page
import unicodedata

#main defs for data extractions

def extract_url_info(url):
    url_segments=url.split('/')


    for segment in url_segments:
        if "for" in segment:
            segment = segment.split('-')
    #        print(segment)
            if len(segment)==5:
                brand = segment[1]
                model = segment[2]
            else:
                del segment[-1]
                del segment [-1]
                del segment [-1]
                del segment [0]
     #       print(segment)
                brand = segment [0]
                if len(segment) == 1:
                    model ="NA"
                elif len(segment) ==2:
                    model = segment[1]
                elif len(segment)>2:
                    model =segment[-2]+" "+segment[-1]
                    if len(segment)>3:
                        brand= brand + " "+segment[1]
                return brand, model

def make_soup(page):
    page = BeautifulSoup(page , "lxml")
    return page



def extract_info(page):
#finding main attributes from car pages
    try:
        info = page.find("div", {"class":"inforight"})
        attributes = info.find_all('span')
        release_date = int(attributes[0].get_text())
        if release_date<1400:
            release_date = release_date + 621
        # these 2 will give Persian names
        #brand = attributes[1].get_text()
        #model = attributes[2].get_text()
        price = attributes[6].get_text()
        if "نوع" not in attributes[8].get_text():
            type = "melli"
            attributes_index = 11
        elif " منطقه آزاد" in attributes[8].get_text():
            type = "mantaqe azad"
            attributes_index = 13
        else:
            type = "gozar movaqaat"
            attributes_index = 13
        mileage = attributes[attributes_index].get_text()
        attributes_index = attributes_index + 2
        gear = attributes[attributes_index].get_text()
        attributes_index = attributes_index+2
        fuel = attributes[attributes_index].get_text()
        attributes_index = attributes_index + 2
        body =  attributes[attributes_index].get_text()
        attributes_index = attributes_index+2
        color = attributes[attributes_index].get_text()
  #  print(release_date)
   # print(brand)
    #print(model)
#    print(price)
 #   print(type)
  #  print(mileage)
   # print(gear)
#       print(fuel)
 #       print(body)
        #print(color)
    except AttributeError:
        print("your car is sold")
        return "NA","NA","NA","NA","NA","NA","NA","NA"


   # finding user defined description for furthur studies
    info = page.find('span',{'itemprop':'description'} )

    try:
        description = info.get_text()
    except AttributeError:
        description = ""
    return description, mileage, price, release_date, gear, fuel, body, color

def extractor(url):
    brand,model = extract_url_info(url)
    try:
        page=open_page(url)
        if isinstance(page, str):
            return
        data=make_soup(page)
    except TypeError:
        return
    extract_info(data)
    try:
        description, mileage, price, release_date, gear, fuel, body_status, color, =extract_info(data)
        return description, mileage, price, release_date, brand, model, gear, fuel, body_status, color
    except:
        print("the car is sold, proceeding to the next url")
        return


extract_url_info("https://bama.ir/car/details-2-6577772/1397-renault-sandero-stepway-at-for-sale")