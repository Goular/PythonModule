import requests

# 代理写法
# proxies = {
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# }
# response = requests.get('https://www.taobao.com', proxies=proxies)
# print(response.status_code)


proxies = {
    'http': 'http://user:password@127.0.0.1:9743'
}
response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
