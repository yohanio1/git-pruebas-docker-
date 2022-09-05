from gettext import find
from msilib.schema import AdminExecuteSequence
from multiprocessing import connection
from tkinter.tix import Tree
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np 
import time, json
from platform import python_branch
import pymongo
from pymongo import errors

articles = []
prices = []
url = []
data = []

def get_data(find_product):

    driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    driver.get("https://www.mercadolibre.com.co")
    search = driver.find_element(By.ID, "cb1-edit")
    search.send_keys(find_product)
    search.send_keys(Keys.ENTER)

    ol = driver.find_element(By.XPATH,"//*[@id='root-app']/div/div[2]/section/ol")
    li = ol.find_elements(By.TAG_NAME,"li")
    cont_prodcuts = np.size(li)

    for i in range (1,(cont_prodcuts+1)):
        item = driver.find_element(By.CSS_SELECTOR,f"li:nth-child({i}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2").text
        url_product = driver.find_element(By.CSS_SELECTOR,f"ol > li:nth-child({i}) > div > div > div.ui-search-result__content-wrapper.shops-custom-secondary-font \
        > div.ui-search-item__group.ui-search-item__group--title.shops__items-group > a").get_attribute("href")
        price = driver.find_element(By.CSS_SELECTOR,f"li:nth-child({i}) > div > div >\
        div.ui-search-result__content-wrapper > div.ui-search-result__content-columns >\
        div.ui-search-result__content-column.ui-search-result__content-column--left >\
        div.ui-search-item__group.ui-search-item__group--price > div > div > div >\
            span.price-tag.ui-search-price__part > span.price-tag-amount > span.price-tag-fraction").text
        
        articles.append(item)
        prices.append(price)
        url.append(url_product)
    
    for i in range (cont_prodcuts):
        data.append({

                "producto" : str(articles[i]),
                "precio": str(prices[i]),
                "url" :  str(url[i])

                                })

    time.sleep(4)
    driver.close()
    return data

def connect_mongo(uri):

    connect = pymongo.MongoClient(uri)

    try:
        connect.web_page.command('ping')
        return connect
    except errors.ConnectionFailure:
        print("Server not available")
        return False
    

def insert_data(webs,connection):

    db = connection["web_page"]
    collection = db["clients"]
    collection.insert_many(webs)


uri = "mongodb://root:pass@localhost:27017"
find_product = "Disco duro de estado sólido"
webs = get_data(find_product)
conection = connect_mongo(uri)
insert_data(webs,conection)

