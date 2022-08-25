from msilib.schema import AdminExecuteSequence
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

#Variable lista para almacenar la información de los  \
#  artículos que se muestra en la página 

articles = []
prices = []

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

# Entrar a la página y buscar el producto "product_name" \
# Dar enter
driver.get("https://www.mercadolibre.com.co")
search = driver.find_element(By.ID, "cb1-edit")
search.send_keys("Ps4")
search.send_keys(Keys.ENTER)

# Buscar la lista no ordenada <ol> con el nombre de los productos 
select = driver.find_element(By.XPATH,"//*[@id='root-app']/div/div[2]/section/ol")
# Seleccionar todos los elementos que contengan la etiqueta li 
li = select.find_elements(By.TAG_NAME,"li")
contador = 0
# Cada vez que se encuentra un elemento de lista se suma \
# en contador 
for line in li:
    contador = contador + 1

# Accediendo al xpath de cada elemento de lista \
#  se identifica 

for i in range (1,(contador+1)):

    if i == 13:
        article = driver.find_element(By.XPATH,f"//*[@id='root-app']/div/div[2] \
        /section/ol/li[{i}]/div/div/div[2]/div[2]/a/h2").text
        price = driver.find_element(By.XPATH,f"//*[@id='root-app']/div/div[2] \
        /section/ol/li[{i}]/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]").text
        prices.append(price)

    else:
        article = driver.find_element(By.XPATH,f"//*[@id='root-app']/div/div[2] \
        /section/ol/li[{i}]/div/div/div[2]/div[1]/a/h2").text
        articles.append (article)
        price = driver.find_element(By.XPATH,f"//*[@id='root-app']/div/div[2] \
        /section/ol/li[{i}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]").text
        prices.append(price)

data = []

for i in range ((contador)):

    data.append({

            "producto" : str(articles[i]),
            "precio": str(prices[i])

                            })

with open("datos_json.json", "w") as archivo_json:
        #escribimos y especificamos la identacion (4 espacios)
        json.dump(data, archivo_json, indent=4)

time.sleep(4)
driver.close()