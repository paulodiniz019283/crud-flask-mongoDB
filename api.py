import requests
from bs4 import BeautifulSoup
import csv

lista_produtos = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url_base = "https://www.kabum.com.br"
start_url = "https://www.kabum.com.br/tv"

page = requests.get(start_url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

tv_pages = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and '/tv' in href:
        tv_pages.append(href)
        
for tv_page in tv_pages:
   
    page_tv = requests.get(tv_page, headers=headers)

    soup_tv = BeautifulSoup(page_tv.content, 'html.parser')


    produtos = soup_tv.find_all('div', class_='sc-1fcmfeb-2 jXZzWW')
    print(produtos)

    for produto in produtos:
        titulo = produto.find('span', class_='sc-d99ca57-0 cpPIRA sc-ff8a9791-16 dubjqF nameCard').text
        preco = produto.find('span', class_='sc-3b515ca1-2 eqqhbT priceCard').text
        preco = preco.replace('\xa0', '').replace(',', '.')
        # print(preco)
        
        produto_dict = {'titulo': titulo, 'preco': preco}
        lista_produtos.append(produto_dict)

    print(len(lista_produtos))
# print(lista)