import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout=0.3)
    print(response.status_code)
except ReadTimeout:
    print('TimeOut')
except HTTPError:
    print('Http Error')
except RequestException:
    print('Error')
