import urllib.request

url = 'http://blog.csdn.net/fungleo/article/details/77575077'

headers = ('User-Agent','Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read().decode('utf-8')
print(data)
fh = open('./mark.html', 'wb')
fh.write(data.encode('utf-8'))
fh.close()
