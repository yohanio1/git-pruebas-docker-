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


driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https://www.bing.com/?setlang=es")
driver.find_element(By.ID,"sb_form_q").send_keys("mongoDB" + Keys.ENTER)

element = str(driver.find_element(By.XPATH,"/html/body/div[1]/main/ol/li[1]").text)
element.split()
print(element)


time.sleep(4)
driver.close()