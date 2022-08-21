from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/home/frank/chromedriver")
driver.get("https://gmail.com")

usuario = driver.find_element(By.ID,"identifierId")
usuario.send_keys("juane.acevedoc@gmail.com")
usuario.send_keys(Keys.RETURN)
time.sleep(3)

driver.close()