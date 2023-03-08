import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.Estudo_MongoDB

     

lista_produtos = []
cont = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

start_url = "https://www.kabum.com.br/busca/monitor-aoc?page_number=" + str(cont) + "&page_size=20&facet_filters=&sort=most_searched"
print(start_url)
page = requests.get(start_url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
url_base = "https://www.kabum.com.br"


while(len(soup.find_all('div', class_="sc-9e19be64-0 jPozmn")) == 0):

    start_url = "https://www.kabum.com.br/busca/monitor-aoc?page_number=" + str(cont) + "&page_size=20&facet_filters=&sort=most_searched"
    cont = cont + 1;
    page = requests.get(start_url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    produtos = soup.find_all('div', class_='sc-ff8a9791-7 hDHAaY productCard')

    for produto in produtos:
        titulo = produto.find('span', class_='sc-d99ca57-0 cpPIRA sc-ff8a9791-16 dubjqF nameCard').text
        #print(titulo)
        product_category = titulo.split(' ')[0]

        if(product_category == "Monitor"):
            if(produto.find('span', class_='sc-3b515ca1-2 eqqhbT priceCard') == None):
                preco = "R$00,0"
                disponibilidade = "Sem estoque"
            else:
                preco = produto.find('span', class_='sc-3b515ca1-2 eqqhbT priceCard').text
                preco = preco.replace('\xa0', '').replace(',', '.')
                disponibilidade = "Disponível"
        
            # url_product_information = url_base + produto.find('a', class_='sc-ff8a9791-10 htpbqG')['href']
            # print(url_product_information)

            # page_url_product_information = requests.get(url_product_information,headers=headers)
            # soup_url_product_information = BeautifulSoup(page.content, 'html.parser')

            # print(soup_url_product_information)
            
            
            
            
            
            produto_dict = {
                'titulo': titulo,
                'preco': preco,
                'disponibilidade': disponibilidade,
                'create_datetime': datetime.datetime.now()
                }
            db.teste.insert_one(produto_dict)
            
            lista_produtos.append(produto_dict)
        
    
    print(len(lista_produtos))
# print(lista)