import urllib.parse
import urllib.request

url = 'http://www.iqianyue.com/mypost'
mydata = urllib.parse.urlencode({
    'name': 'Goualr',
    'pass': 'zhao@3698741'
}).encode(encoding='utf-8')
req = urllib.request.Request(url, mydata)
data = urllib.request.urlopen(req).read()
print(data)
fh = open('./post.html', 'wb')
fh.write(data)
fh.close()
