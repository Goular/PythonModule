# urlopen
import urllib.parse
import urllib.request
import urllib.error
import socket

# 普通提交
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# 用于编辑POST访问的查询字符串
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# 超时访问设置
# response = urllib.request.urlopen('http://www.httpbin.org/get', timeout=1)
# print(response.read().decode('utf-8'))

# 访问进行错误处理
# try:
#     response = urllib.request.urlopen('http://www.httpbin.org/get', timeout=1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')
# except Exception as err:
#     print("")
# finally:
#     print('End')
