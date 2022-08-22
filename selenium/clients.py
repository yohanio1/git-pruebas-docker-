from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
with open("clients.json") as json_file:
    data = json.load(json_file)
    driver.get("https://my.forms.app/form/6303956676ece330d75fe470")
    name = driver.find_element(By.XPATH,"//*[@id='i-text-1']")
    name.send_keys(1)
    time.sleep(3)
    driver.get("https://my.forms.app/form/6303956676ece330d75fe470")
    name = driver.find_element(By.XPATH,"//*[@id='i-text-1']")
    name.send_keys(1)
    time.sleep(3)

driver.close()

        

# name = driver.find_element(By.XPATH,"//*[@id='i-text-1']")
# last_name = driver.find_element(By.XPATH,"//*[@id='i-text-2']")
# name.send_keys("Juan")
# last_name.send_keys("Acevedo")
# time.sleep(3)
# driver.close()

# with open("clients.json") as json_file:
#     data = json.load(json_file)

#     for dato in data["clients"]:
#         print("Escribiendo datos de + " + dato["name"])
#         driver.get("https://www.google.com.co")
#         name = driver.find_element(By.XPATH,"//*[@id='i-text-1']")
#         last_name = driver.find_element(By.XPATH,"//*[@id='i-text-2']")
#         # name.send_keys(dato["name"])
#         # last_name.send_keys(dato["last_name"])
#         time.sleep(3)
        
