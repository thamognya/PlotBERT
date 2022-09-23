from lib2to3.pgen2 import driver
from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# set options
opts = Options()
opts.set_preference("browser.download.dir", "/home/jeff/Documents/gitRepos/PlotBERT/data/")
browser = webdriver.Firefox(options=opts)

class ScrapeClass:

    def __init__(self, n = 0):
        self.n = n
    
    def setNumberOfBooks(self, n):
        self.n = n

