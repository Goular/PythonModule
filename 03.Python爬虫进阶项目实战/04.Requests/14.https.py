import requests
import urllib3
import logging

# response = requests.get('https://www.12306.cn')
# print(response.status_code)

# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)

# response = requests.get('https://www.12306.cn', verify=False)
# urllib3.disable_warnings()
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)

response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)
