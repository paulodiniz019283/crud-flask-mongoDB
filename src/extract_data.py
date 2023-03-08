from bs4 import BeautifulSoup

class ExtractData:
    def __init__(self):
        pass
    
    def connect_retailer_(self, start_url):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        page = requests.get(start_url,headers=headers)
    

        