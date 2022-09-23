from lib2to3.pgen2 import driver
from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import re

"""
Resources:
- https://selenium-python.readthedocs.io/locating-elements.html
"""

# set options
opts = Options()
opts.set_preference("browser.download.dir", "/home/jeff/Documents/gitRepos/PlotBERT/data/")
opts.headless = True
driver = webdriver.Firefox(options=opts)

class ScrapeClass:

    def __init__(self, n = 0, url=""):
        self.n = n
        self.url = url
    
    def setNumberOfBooks(self, n):
        self.n = n

    def getZLibUrl(self):
        driver.get("https://z-lib.org")
        redirectedLink = driver.find_element(By.CSS_SELECTOR, "a.domain-check-link").get_attribute("href")
        self.url = redirectedLink
        return redirectedLink

    def openZLibUrl(self):
        self.getZLibUrl()
        driver.get(self.url)
        arraysOfBooks = driver.find_elements(By.CSS_SELECTOR, "a.book-loading")
        linkOfBooks = []
        for book in arraysOfBooks:
            linkOfBooks.append(book.get_attribute("href"))
        return linkOfBooks

scrapeTest = ScrapeClass()
print(scrapeTest.openZLibUrl())