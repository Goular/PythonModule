import http.cookiejar, urllib.request

# 获取返回的cookie
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)

# 获取并保存cookie并保存到cookie.txt,便于后面的调用
# import http.cookiejar, urllib.request
#
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# # 忽略和没有的不保存
# cookie.save(ignore_discard=True, ignore_expires=True)

# 两种格式都是不一样的
# import http.cookiejar, urllib.request
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# # 忽略和没有的不保存
# cookie.save(ignore_discard=True, ignore_expires=True)

# 两种格式都是不一样的
import http.cookiejar, urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
