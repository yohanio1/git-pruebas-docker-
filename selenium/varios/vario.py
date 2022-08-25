from lib2to3.pgen2 import driver
from time import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# wait max 10 seconds
driver = webdriver.Edge("C:\driver\msedgedriver")
driver.get("https://www.plupload.com/examples/")

element = driver.find_element(By.XPATH,"/html/body/section/div/div[4]/div/div/div/table[2]/tbody/tr/td[1]/div[1]")
element.send_keys("C:\\Users\\juane\\Downloads\\Image_created_with_a_mobile_phone.png")


driver.close()