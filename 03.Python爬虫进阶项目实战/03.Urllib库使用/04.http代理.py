import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://61.135.217.7',
    'https': 'https://39.71.173.216:8123',
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
print(response.read())
