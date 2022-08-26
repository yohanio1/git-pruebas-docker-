from lib2to3.pgen2 import driver
import time
import unittest
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    
    def tearDown(self):
        self.driver.close()


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
    
    def test_search_in_xchrome(self):   
        driver = self.driver
        driver.get("http://www.google.com.co")
        elem = driver.find_element(By.NAME,"q")
        elem.send_keys("Hola esto es una prueba")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Ver todos", driver.page_source)

    def test_search_by_xpath(self):   
        driver = self.driver
        driver.get("http://www.google.com.co")
        elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        elem.send_keys("Hola esto es una prueba")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Ver todos", driver.page_source)

    def test_change_window(self):   

        driver = self.driver
        driver.get("http://www.google.com.co")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://accounts.google.com")
        elem = driver.find_element(By.XPATH,"//*[@id='identifierId']")
        elem.send_keys("juane.acevedoc@gmail.com")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

    def test_back_forward(self):   

        driver = self.driver
        driver.get("http://www.google.com.co")
        time.sleep(3)
        driver.get("https://www.youtube.com")
        time.sleep(3)
        driver.back()

    def test_toggle_click(self):   

        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        select = driver.find_element(By.XPATH,"//*[@id='main']/label[3]/div")
        select.click()
        time.sleep(3)
        select.click()
        time.sleep(3)
        

    def test_select_list(self):   

        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        select = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select")
        options = select.find_elements(By.TAG_NAME,"option")
                                                                            
        for option in options:
            print(option.get_attribute("value"))

        seleccionar = Select(driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("2")


if __name__ == "__main__":
    unittest.main()
