import urllib.request


def use_proxy(url, proxy_url):
    proxy = urllib.request.ProxyHandler({'http': proxy_url})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    return data


proxy_url = '61.155.164.107:3128'
url = 'http://www.baidu.com'
data = use_proxy(url, proxy_url)
print(data)
