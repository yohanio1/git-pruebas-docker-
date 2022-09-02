from gettext import find
from msilib.schema import AdminExecuteSequence
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

articles = []
prices = []
url = []
data = []

def get_data():

    driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    driver.get("https://www.mercadolibre.com.co")
    search = driver.find_element(By.ID, "cb1-edit")
    search.send_keys("Disco duro estado sólido")
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
    
    for i in range (6):
        data.append({

                "producto" : str(articles[i]),
                "precio": str(prices[i]),
                "url" :  str(url[i])

                                })

    time.sleep(4)
    driver.close()
    return data


def connect_mongo(webs):
    client = pymongo.MongoClient(host='localhost',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["web_page"]
    collection = db["clients"]
    collection.insert_many(webs)


data = get_data()
connect_mongo(data)

