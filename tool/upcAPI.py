import requests
from bs4 import BeautifulSoup
class upcAPI:
    API_ROOT = 'http://www.upcitemdb.com/upc/'
    def __init__(self):
        self.br = requests.Session()
    
    def search(search, upc=''):
        r =search.br.get(search.API_ROOT+str(upc))
        soup = BeautifulSoup(r.content,'html.parser')
        
        
        for ol_tag in soup.find_all('ol',{'class':'num'}):
            for li_tag in ol_tag.find_all('li'):
                if li_tag.text:
                    return li_tag.text
    

        
        
        

if __name__ == '__main__':
    a = upcAPI()
    a.search('8806146941717')