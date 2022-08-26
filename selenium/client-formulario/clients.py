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
