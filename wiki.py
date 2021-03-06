from selenium import webdriver
from locators import WikipediaHomepages,WikipediaArticle
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome('./chromedriver')
driver.get('https://en.wikipedia.org')

random_link=driver.find_element(*WikipediaHomepages.Random_Link)
random_link.click()

time.sleep(4)

first_heading=driver.find_element(*WikipediaArticle.First_Heading)
print(first_heading.text)
page_info=driver.find_element(*WikipediaArticle.Page_Info)
page_info.click();

time.sleep(5)

search_box=driver.find_element(*WikipediaArticle.Search_Box)
search_box.send_keys('Selenium (software)' + Keys.RETURN)

time.sleep(5)

logo=driver.find_element(*WikipediaArticle.Logo)
logo.click();

driver.quit()