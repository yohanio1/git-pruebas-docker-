from lib2to3.pgen2 import driver
import time
from typing_extensions import Self
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class GmailTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    
    def tearDown(self):
        self.driver.close()


    def test_gmailOrg(self):

        driver = self.driver
        driver.get("https://gmail.com")
        usuario = driver.find_element(By.ID,"identifierId").size
        usuario.send_keys("juane.acevedoc@gmail.com")
        usuario.send_keys(Keys.RETURN)
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()