# from urllib import request, error
#
# try:
#     response = request.urlopen('http://cuiqingci.com/index.html')
# except error.URLError as e:
#     print(e.reason)
#

# from urllib import request, error
#
# try:
#     response = request.urlopen('http://fdsfdsfds.com/index.htm')
# except error.HTTPError as err:
#     print(err.reason, err.code, err.headers, sep='\n')
# except error.URLError as err:
#     print(err.reason)
# else:
#     print("Request Successfuly")

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://www.sdfdsfsdfds.com', timeout=1)
except urllib.error.URLError as err:
    print(type(err))
    print(err)
    if isinstance(err.reason,socket.timeout):
        print('Time Out')