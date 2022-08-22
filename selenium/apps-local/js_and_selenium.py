from msilib.schema import AdminExecuteSequence
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")

driver.get("https://www.google.com.co")
driver.execute_script("console.log('Hola')")
driver.execute_script("window.open('https://www.youtube.com')")
driver.switch_to.window(driver.window_handles[1])
driver.execute_script("console.log('Adios')")

time.sleep(20)

driver.close()