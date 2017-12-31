import urllib.request

url = 'http://www.hellobi.com'
obj = urllib.request.urlopen(url)
info = obj.info()
url = obj.geturl()
code = obj.getcode()
print(info)
print(code)
print(url)
