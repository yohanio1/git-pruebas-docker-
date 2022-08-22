from msilib.schema import AdminExecuteSequence
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

USER = "admin"
PASSWORD = "Juanest31"

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https:/www.google.com.co")
search = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys("python")
search.send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a/h3").click()
driver.find_element(By.LINK_TEXT,"Docs").click()
driver.find_element(By.LINK_TEXT,"What's new in Python 3.10?").click()

# password = driver.find_element(By.XPATH,"//*[@id='password']")
# password.send_keys(PASSWORD)
# password.send_keys(Keys.ENTER)

time.sleep(5)
driver.close()