# 写法一
# import urllib
# from urllib.request import urlopen
#
# data = urlopen("http://www.baidu.com").read()
# print(data)

# 写法二
from urllib import request

data = request.urlopen("https://music.jiagongwu.com").read()
print(data)
