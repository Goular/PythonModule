import requests

response = requests.get('https://www.baidu.com')
print(type(response))
print(type(response.status_code))
print(type(response.text))
print(response.text)
print(response.cookies)
