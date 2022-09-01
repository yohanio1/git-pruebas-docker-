import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def create_test(project_key,key):
    driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    driver.get("http://localhost:9000/sessions/new?return_to=%2F")
    driver.set_window_size(1050, 700)
    driver.find_element(By.ID, "login").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("Juanest31")
    driver.find_element(By.CSS_SELECTOR, ".button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div > button").click()
    driver.find_element(By.XPATH," //*[@id='projects-page']/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/ul/li/a").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#project-key").send_keys(project_key)
    driver.find_element(By.CSS_SELECTOR, "#create-project > div > div > form > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > div > form > input").send_keys(key)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > div > form > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div:nth-child(3) > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div > div:nth-child(1) > ul > li:nth-child(4) > label").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div > div.big-spacer-top > ul > li:nth-child(2) > label").click()
    time.sleep(1)
    clave = driver.find_element(By.XPATH,"//*[@id='container']/div/div/div/div[3]/div[3]/div/div/div[3]/div/div[2]/div/button")
    data = str(clave.get_attribute("data-clipboard-text")).split("-D")
    driver.close()
    return data

def create_txt(data,key):
    with open("selenium\\sonar\\test.txt",'w',encoding = 'utf-8') as file:
        for dato in data:
            file.write(dato.strip('"') + "\n")
        file.write("Key:" + key + "\n")


#................................. Main ...................................................................
project_key = "XM_PROJECT_WITH_SELENIUM4"
key = "SECRETO3"

data = create_test(project_key,key)
create_txt(data,key)
