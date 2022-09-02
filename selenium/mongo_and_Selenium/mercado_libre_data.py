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

time.sleep(4)
driver.close()

# print(articles)
# print(prices)

data = []

for i in range (cont_prodcuts):
    data.append({

            "producto" : str(articles[i]),
            "precio": str(prices[i]),
            "url" :  str(url[i])

                            })

# with open("datos_json.json", "w") as archivo_json:
#         #escribimos y especificamos la identacion (4 espacios)
#         json.dump(data, archivo_json, indent=4)

def connect_mongo(webs):
    data_list = []
    host = "localhost"
    user = "root"
    password = "example"
    port = 27017
    client = pymongo.MongoClient('mongodb://%s:%s@%s:%s/' % (user,password,host,port))
    mydb = client["web_page"]
    mycol = mydb["client"]
    mycol.insert_many(webs)
    for documents in mycol.find():
        data_list.append(documents)


connect_mongo(data)

