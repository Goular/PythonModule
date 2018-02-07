import requests

# 例子一: 会直接报错500
# response = requests.get('https://www.zhihu.com/explore')
# print(response.text)

# 例子二
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
response = requests.get("https://www.zhihu.com/explore", headers=headers)

