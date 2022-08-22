from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
with open("./clients.json") as json_file:
    data = json.load(json_file)

    for dato in data["clients"]:
        driver.get("https://www.w3schools.com/html/html_forms.asp")
        name = driver.find_element(By.XPATH,"//*[@id='fname']")
        name.click()
        name.clear()
        name.send_keys(dato["name"])

        name2= driver.find_element(By.XPATH,"//*[@id='lname']")
        name2.click()
        name2.clear()
        name2.send_keys(dato["last_name"])
        name2.send_keys(Keys.ENTER)

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
        
