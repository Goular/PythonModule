import requests

# response = requests.get('http://httpbin.org/get', timeout=1)
# print(response.status_code)


import requests
from requests.exceptions import ReadTimeout

try:
    response = requests.get('http://httpbin.org/get', timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
