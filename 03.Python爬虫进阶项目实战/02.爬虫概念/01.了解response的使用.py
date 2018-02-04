import requests;
response = requests.get('http://www.baidu.com')
# 打印响应体
print(response.text)
# 打印响应码
print(response.status_code)
# 打印响应头
print(response.headers)