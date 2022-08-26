import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", True)
service = ChromeService(executable_path="C:\driver\chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://postimages.org")
# user = driver.find_element(By.XPATH,"/html/body")
# user.send_keys(Keys.CONTROL+ "v")

driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
first_name = driver.find_element(By.XPATH,"//*[@id='mainContent'] \
/div[6]/div/form/table/tbody/tr[1]/td[2]/input")
first_name.send_keys("Juan Esteban")

last_name = driver.find_element(By.XPATH,"//*[@id='mainContent'] \
/div[6]/div/form/table/tbody/tr[2]/td[2]/input")
last_name.send_keys("Acevedo Carmona")

list_sex = driver.find_element(By.XPATH,"//*[@id='mainContent'] \
/div[6]/div/form/table/tbody/tr[3]/td[2]")
sex_option = list_sex.find_elements(By.TAG_NAME,"input")
sex_option[0].click()

list_experience = driver.find_element(By.XPATH,"//*[@id='mainContent'] \
/div[6]/div/form/table/tbody/tr[4]/td[2]")
option_experience = list_experience.find_elements(By.TAG_NAME,"span")
option_experience[4].click()


date = driver.find_element(By.XPATH,"//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[5]/td[2]/input")
date.send_keys("03/08/2000")

# driver.find_element(By.XPATH,"///*[@id='mainContent']/div[6]/div/form/table/tbody/tr[6]/td[2]/span[1]/input").click

driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2) > span:nth-child(2) > input[type=checkbox]").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) > td:nth-child(2) > span:nth-child(3) > input[type=checkbox]").click()
driver.find_element(By.XPATH,"//input[@type='file']").send_keys("C:\\Users\\juane\\Downloads\\Image_created_with_a_mobile_phone.png")

# select = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[6]/div/form/table/tbody/tr[8]/td[2]")
# seleccion = select.find_elements(By.TAG_NAME,"span")
# print(seleccion[2].text)

list_continent = driver.find_element(By.XPATH,"//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[9]/td[2]/select")
options_continent = list_continent.find_elements(By.TAG_NAME,"option")
options_continent[3].click()

list_command = driver.find_element(By.XPATH,"//*[@id='mainContent']/div[6]/div/form/table/tbody/tr[10]/td[2]/select")
option_command = list_command.find_elements(By.TAG_NAME,"option")
option_command[3].click()

time.sleep(6) 


driver.close()