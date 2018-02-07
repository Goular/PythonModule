import requests

response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == requests.codes.ok else print('Request Successfully')
