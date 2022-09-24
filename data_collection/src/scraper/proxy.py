from this import d
from proxy_randomizer import RegisteredProviders
import requests

rp = RegisteredProviders()
rp.parse_providers()

class ProxyClass:

    def getProxy(self):
        proxy = rp.get_random_proxy()
        return [proxy.ip_address, proxy.port, proxy.ip_address + ":" + proxy.port]

proxy = ProxyClass()
print(proxy.getProxy())