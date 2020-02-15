from selenium.webdriver.common.by import By

class WikipediaHomepages(object):
    Random_Link=(By.CSS_SELECTOR,'#n-randompage')

class WikipediaArticle(object):
    First_Heading=(By.CSS_SELECTOR,'.firstHeading')
    Page_Info=(By.LINK_TEXT,'Page information')
    Search_Box=(By.NAME,'search')