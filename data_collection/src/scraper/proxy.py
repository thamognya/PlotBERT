from proxy_randomizer import RegisteredProviders
from dotenv import load_dotenv, find_dotenv
import os
import requests

rp = RegisteredProviders()
rp.parse_providers()

class ProxyClass:

    def getProxy(self):
        load_dotenv(find_dotenv()) 
        SCRAPER_API = os.environ.get("SCRAPER_API")
        return f'http://scraperapi:{SCRAPER_API}@proxy-server.scraperapi.com:8001'