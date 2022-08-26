from lib2to3.pgen2 import driver
import time
from typing_extensions import Self
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    
    def tearDown(self):
        self.driver.close()


# Exercise 1
# - Open the Firefox browser.
# - Maximize the browser window.
# - Navigate to “http://qatechhub.com”.
# - Write a method to print PASS if the title of the page matches with “QA Automation Tools Trainings and Tutorials | QA Tech Hub” else FAIL. (If you are familiar with TestNG or JUnit use assert statement like assert.assertequals(actual, expected) to give a verdict of the pass or fail status.
# - Navigate to the Facebook page (https://www.facebook.com)
# - Navigate back to the QA Tech Hub website.
# - Print the URL of the current page.
# - Navigate forward.
# - Reload the page.
# - Close the Browser.


    def test_exercise1(self):
        driver = self.driver

        driver.maximize_window()
        driver.get("http://qatechhub.com")
        get_title = driver.title

        if get_title == "QA Automation Tools Trainings and Tutorials | QA Tech Hub":
            print("PASS")
        else:
            print("FAIL")

        driver.execute_script("window.open('https://www.facebook.com');")
        driver.switch_to.window(driver.window_handles[1])
        print(driver.current_url)
        time.sleep(5)
        driver.refresh()
        time.sleep(5)

# Exercise 2

# Open any browser of your choice (Mozilla firefox, Chrome, Internet Explorer or Safari). Write the code in such a way that based on argument passed respective browser is selected.
# Browse to https://in.ebay.com/ website.
# Enter a product in the search box on the homepage (say Apple Watches).
# From categories dropdown, select category of your product (say Electronics).
# Click the Search button.
# Write a method to print the result of the product.
# Write a method to print Nth product say 10th Product. (This should be a generic method)
# Write a method to print all products from 1st page.
# Write a method to print all products along with scroll down.


    def test_exercise2(self):
        driver = self.driver
        driver.get("https://www.ebay.com")
        search = driver.find_element(By.XPATH,"//*[@id='gh-ac']")
        search.send_keys("moto")
        
        select = driver.find_element(By.XPATH,"/html/body/header/table/tbody/tr/td[3] \
        /form/table/tbody/tr/td[2]/div/select")

        options = select.find_elements(By.TAG_NAME,"option")
        options[17].click()
        
        driver.find_element(By.XPATH,"/html/body/header/table/tbody/tr/td[3] \
        /form/table/tbody/tr/td[3]/input").click()

        scroll_init= 0
        scroll_final = 200
        
        for i in range(10):
            driver.execute_script(f"window.scrollTo({scroll_init},{scroll_final} );")
            scroll_init = scroll_final
            scroll_final = scroll_final + 250
            time.sleep(1)


    # exercise 3
    # – Open any browser of your choice, for example, Chrome Browser.
    # – Navigate to Snapdeal site (http://www.snapdeal.com)
    # Sign_in_button
    # – Move to Sign In Button and hold
    # – Move to the Sign In button and click.
    # – Enter valid Email Id and click continue.
    # – Enter the valid password and click LOGIN.
    # – Verify that the user is logged in successfully.

    def test_exercise_3(self):  

        driver = self.driver
        driver.get("https://seleniumplayground.practiceprobs.com/contact/")
        driver.find_element(By.CSS_SELECTOR,"#contact-form > p:nth-child(2) > label > input[type=text]").\
        send_keys("Juan Esteban Acevedo Carmona")
        driver.find_element(By.CSS_SELECTOR,"#contact-form > p:nth-child(3) > label > input[type=email]").\
        send_keys("juane.acevedoc@gmail.com")
        select = driver.find_element(By.XPATH,"//*[@id='contact-form']/p[3]/label/select")
        options = select.find_elements(By.TAG_NAME,"option")
        options[4].click()
        driver.find_element(By.CSS_SELECTOR,"p:nth-child(5) > label > input[type=file]").send_keys("C:\\Users\\juane\\Downloads\\Image_created_with_a_mobile_phone.png")
        driver.find_element(By.CSS_SELECTOR,"p:nth-child(6) > label > textarea").send_keys("Exitos")
        driver.find_element(By.XPATH,"//*[@id='contact-form']/p[6]/button").click()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()