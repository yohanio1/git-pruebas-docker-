from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

#Variable lista para almacenar la información de los  \
#  artículos que se muestra en la página 

articles = []
prices = []

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.find_element(By.XPATH,"/html/body/div[3]/main/div/div[3]/article/div/form/p[4]/label/input")


driver.close()