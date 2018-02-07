import requests

# data = {
#     'name': 'Goular8888',
#     'age': 236
# }
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)


# 带Header的POST请求
data = {
    'name': 'Goular88889',
    'age': 2360
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.json())
