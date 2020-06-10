import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from selenium import webdriver
# firefox_options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(firefox_options=firefox_options)
driver= webdriver.Chrome(executable_path='./chromedriver')

class MonsterJobScrapper:

    def createUrl(self, jobTitle, location):
        test_url = "https://www.monsterindia.com/srp/results?query={}&locations={}&searchId=754af010-3ca4-4df6-bbc6-eb3c88da1f77".format(jobTitle, location)
        return test_url

    def get_webPage(self, test_url):
        driver.get(test_url)
        driver.implicitly_wait(30)
        source = driver.page_source
        html = bs(source, "html.parser")
        bigboxes = html.findAll("div", {"class": "card-apply-content"})
        return bigboxes


