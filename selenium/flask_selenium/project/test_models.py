from lib2to3.pgen2 import driver
from math import prod
import time
import unittest
import mongo_and_MercadoLibre
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Connection(unittest.TestCase):

    def test_connectionDB(self):
        uri = "mongodb://root:pass@localhost:27017"
        self.assertIn("connect=True",str(mongo_and_MercadoLibre.connect_mongo(uri)))

    def test_invalidURI(self):
        uri = "mongodb://root:pass@localhost:27018"
        self.assertEqual(mongo_and_MercadoLibre.connect_mongo(uri),False)

    def test_listdDictInfo(self):
        product = "PS4"
        self.assertIsInstance(mongo_and_MercadoLibre.get_data(product),list)
    
    def test_dropDB(self):
        uri = "mongodb://root:pass@localhost:27017"
        conection = mongo_and_MercadoLibre.connect_mongo(uri)
        res = mongo_and_MercadoLibre.delete_data(conection)
        self.assertEqual(list(res),list())

        
if __name__ == "__main__":
    unittest.main()

