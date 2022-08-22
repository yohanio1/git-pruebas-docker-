from msilib.schema import AdminExecuteSequence
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json


driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https://github.com/")

driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a").click()
time.sleep(3)

user = driver.find_element(By.XPATH,"//*[@id='login_field']")
user.send_keys("yohanio1")
password = driver.find_element(By.XPATH,"//*[@id='password']")
password.send_keys("juanesteban4348310771173408")
password.send_keys(Keys.ENTER)
time.sleep(3)
## Click en el repositorio
driver.find_element(By.XPATH,"/html/body/div[5]/div/aside/div/div[1]/div/ul/li[1]/div/div/a").click()
time.sleep(3)
## Click a code
driver.find_element(By.XPATH,"//*[@id='repo-content-pjax-container']/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/summary").click()
time.sleep(3)
## Click a copiar
driver.find_element(By.XPATH,"//*[@id='repo-content-pjax-container']/div/div/div[3]/div[1]/div[2]/span/get-repo/feature-callout/details/div/div/div[1]/ul/li[1]/tab-container/div[2]/div/div/clipboard-copy").click()
time.sleep(3)

driver.close()