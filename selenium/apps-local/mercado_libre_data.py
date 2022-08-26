from gettext import find
from msilib.schema import AdminExecuteSequence
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, json

articles = []
prices = []

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https://www.mercadolibre.com.co")
search = driver.find_element(By.ID, "cb1-edit")
search.send_keys("Disco duro estado sólido")
search.send_keys(Keys.ENTER)

ol = driver.find_element(By.XPATH,"//*[@id='root-app']/div/div[2]/section/ol")
li = ol.find_elements(By.TAG_NAME,"li")

cont_li = 0

for element in li:
        cont_li = cont_li + 1

for i in range (1,(cont_li+1)):
    item = driver.find_element(By.CSS_SELECTOR,f"li:nth-child({i}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2").text
    
    price = driver.find_element(By.CSS_SELECTOR,f"li:nth-child({i}) > div > div >\
     div.ui-search-result__content-wrapper > div.ui-search-result__content-columns >\
      div.ui-search-result__content-column.ui-search-result__content-column--left >\
       div.ui-search-item__group.ui-search-item__group--price > div > div > div >\
        span.price-tag.ui-search-price__part > span.price-tag-amount > span.price-tag-fraction").text
    
    articles.append(item)
    prices.append(price)

# print(articles)
# print(prices)

data = []

for i in range (cont_li):
    data.append({

            "producto" : str(articles[i]),
            "precio": str(prices[i])

                            })

with open("selenium\\apps-local\\datos_json.json", "w") as archivo_json:
        #escribimos y especificamos la identacion (4 espacios)
        json.dump(data, archivo_json, indent=4)

time.sleep(4)
driver.close()