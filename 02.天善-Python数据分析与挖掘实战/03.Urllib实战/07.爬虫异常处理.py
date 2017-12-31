import urllib.error
import urllib.request

try:
    urllib.request.urlopen('http://1256.blog.csdn.net')
except urllib.error.URLError as err:
    if hasattr(err, 'code'):
        print(err.code)
    if hasattr(err, 'reason'):
        print(err.reason)
