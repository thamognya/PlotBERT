from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import DesiredCapabilities
from fake_useragent import UserAgent
import time
import proxy

"""
Resources:
- https://selenium-python.readthedocs.io/locating-elements.html
"""

# set options
srv=Service(ChromeDriverManager().install())
ua = UserAgent()
opts = Options()
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-sh-usage')
# opts.set_preference("browser.download.dir", "/home/jeff/Documents/gitRepos/PlotBERT/data/")
# opts.headless = True

proxyClass = proxy.ProxyClass()
WAIT = 20

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

    def downloadBooks(self, driver, url):
        return "hello"

    def openZLibUrl(self):
        for i in range(self.n):
            if (i % 5 == 0):
                PROXY = proxyClass.getProxy()
            proxy_options = {
                'proxy': {
                    'http': PROXY,
                    'no_proxy': 'localhost,127.0.0.1'
                }
            }
            userAgent = ua.random
            opts.add_argument(f'user-agent={userAgent}')

            driver = webdriver.Chrome(options=opts, service=srv, seleniumwire_options=proxy_options)
            # driver.get('https://ipleak.net')
            self.getZLibUrl(driver)
            print(self.url)
            # driver.get(self.url)
            # arraysOfBooks = driver.find_elements(By.CSS_SELECTOR, "a.book-loading")
            # i = 0
            # for book in arraysOfBooks:
            #     self.linkOfBooks.append(book.get_attribute("href"))
            #     i += 1
            #     if (i == 5): 
            #         break
            if (i != self.n - 1):
                time.sleep(WAIT)

        return self.linkOfBooks

scrapeTest = ScrapeClass()
scrapeTest.setNumberOfBooks(2) # n * 5
print(scrapeTest.openZLibUrl())