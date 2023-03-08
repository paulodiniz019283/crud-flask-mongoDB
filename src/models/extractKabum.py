from pymongo import MongoClient

class kabumModel:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.Data_Mining

    def insert_product(self, produto_dict):
        self.db.Products_Kabum.insert_one(produto_dict)

    def close_connection(self):
        self.client.close()
        