import requests

# 写法一
# response = requests.get('http://httpbin.org/get?name=germary&age=28')
# print(response.text)


# 写法二
data = {
    'name': 'Goular',
    'age': 26
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
