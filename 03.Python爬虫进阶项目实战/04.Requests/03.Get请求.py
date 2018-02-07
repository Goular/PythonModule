import requests

# 普通的get请求
response = requests.get('http://httpbin.org/get')
print(response.text)