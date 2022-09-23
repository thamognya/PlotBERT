from proxy_randomizer import RegisteredProviders
import requests

rp = RegisteredProviders()
rp.parse_providers()

for proxy in rp.proxies:
    proxies = {"https": proxy.get_proxy()}
    print(proxies)