import urllib.request

param = 'python'
param = urllib.request.quote(param)
url = 'http://www.baidu.com/s?wd='
req = urllib.request.Request(url + param)
data = urllib.request.urlopen(req).read()
print(data)
fh = open('./get.html', 'wb')
fh.write(data)
fh.close()
