from html.parser import HTMLParser
from urllib import parse


#my class extends html parser
class LinkFinder(HTMLParser):

#constructor
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url= base_url
        self.page_url = page_url
        self.links= set()



    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for(attribute,value) in attrs:
                if attribute =='href':
                        url = parse.urljoin(self.base_url, value)
                        if "page" in url:
                            self.links.add(url)
                            print(url)
                        if "details" in url:
                            self.links.add(url)
                            print(url)



    def page_links(self):
        return self.links

