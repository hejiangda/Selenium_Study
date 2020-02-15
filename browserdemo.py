import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.seleniumhq.org')

print(driver.title)

time.sleep(20)
driver.quit()