from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.firefox.webdriver.WebDriver()
driver.get("https://www.google.com")
input_fields = driver.find_element_by_name('q')
input_fields.send_keys('python')
time.sleep(2)
input_fields.send_keys(Keys.DOWN)
#input_fields.send_keys(Keys.DOWN)
input_fields.send_keys(Keys.ENTER)
time.sleep(2)

# titles = driver.find_elements_by_class_name('g')
# for title in titles:
# 	print(title.text)
# 	print('\n')

titles = driver.find_elements(By.XPATH, '//h3')
for title in titles:
 	print(title.text)
 	print('\n')

driver.quit()
