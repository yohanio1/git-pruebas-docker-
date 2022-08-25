from lib2to3.pgen2 import driver
import time
from typing_extensions import Self
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome("C:\driver\chromedriver")

driver.get("https://seleniumplayground.practiceprobs.com/contact/")
driver.find_element(By.XPATH,"/html/body/div[3]/main/div/div[3]/article/div/form/p[4]/label/input").click()

time.sleep(5)

driver.close()