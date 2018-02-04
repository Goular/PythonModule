from urllib import request, parse
import urllib.request

# 使用但是做一个request对象，然后带着对象进行访问
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# headers变更User-Agent提交
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Goular'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# header的另一种写法,但是稚嫩刚添加一个header
url = 'http://httpbin.org/post'
dict = {
    'name': 'Goular8868'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
