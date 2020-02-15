from selenium import webdriver
from locators import WikipediaHomepages
import time

driver=webdriver.Chrome('./chromedriver')
driver.get('https://en.wikipedia.org')

random_link=driver.find_element(*WikipediaHomepages.Random_Link)
random_link.click()

time.sleep(4)

print(driver.title)
driver.quit()