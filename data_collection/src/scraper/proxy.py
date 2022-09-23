from proxy_randomizer import RegisteredProviders
import requests

rp = RegisteredProviders()
rp.parse_providers()

class ProxyList:

    def getProxies(self, n):
        proxies = []
        proxies.append(rp.get_random_proxy())
        return proxies