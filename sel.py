# from selenium import webdriver
 
# driver = webdriver.Firefox()
# driver.get("http://google.com")
# assert "Google" in driver.page_sourse
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Firefox()
driver = webdriver.firefox.webdriver.WebDriver()
driver.get("https://www.google.com")
input_fields = driver.find_element_by_name('q')
input_fields.send_keys('python')
time.sleep(2)
input_fields.send_keys(Keys.DOWN)
input_fields.send_keys(Keys.DOWN)
input_fields.send_keys(Keys.ENTER)

time.sleep(2)

titles = driver.find_elements_by_class_name('g')
for title in titles:
	assert "Python" in title.text.lower()


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
#driver.close()