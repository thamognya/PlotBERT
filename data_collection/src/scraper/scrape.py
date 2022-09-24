from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import DesiredCapabilities
import proxy

"""
Resources:
- https://selenium-python.readthedocs.io/locating-elements.html
"""

# set options
opts = Options()
opts.set_preference("browser.download.dir", "/home/jeff/Documents/gitRepos/PlotBERT/data/")
opts.headless = True

proxyClass = proxy.ProxyClass()

class ScrapeClass:

    def __init__(self, n = 0, url="", linkOfBooks = []):
        self.n = n
        self.url = url
        self.linkOfBooks = linkOfBooks
    
    def setNumberOfBooks(self, n):
        self.n = n

    def getZLibUrl(self, driver):
        driver.get("https://z-lib.org")
        redirectedLink = driver.find_element(By.CSS_SELECTOR, "a.domain-check-link").get_attribute("href")
        self.url = redirectedLink
        return redirectedLink

    def downloadBooks(self, url):
        return "hello"

    def openZLibUrl(self):
        firefox_capabilities = DesiredCapabilities().FIREFOX
        for i in range(self.n):
            if (i % 5 == 0):
                myProxy = proxyClass.getProxy()
                firefox_proxies = Proxy()
                firefox_proxies.ssl_proxy = myProxy[2]
                firefox_proxies.add_to_capabilities(firefox_capabilities)
            # TODO: add proxy to webdriver somehow
            print(myProxy)
            driver = webdriver.Firefox(options=opts, desired_capabilities=firefox_capabilities)
            self.getZLibUrl(driver)
            driver.get(self.url)
            arraysOfBooks = driver.find_elements(By.CSS_SELECTOR, "a.book-loading")
            i = 0
            for book in arraysOfBooks:
                self.linkOfBooks.append(book.get_attribute("href"))
                i += 1
                if (i == 5): 
                    break
        return self.linkOfBooks

scrapeTest = ScrapeClass()
scrapeTest.setNumberOfBooks(1)
print(scrapeTest.openZLibUrl())