# import urllib.request
#
# url = 'http://www.hellobi.com'
# file = urllib.request.urlopen(url, timeout=0.1) # 直接报错


import urllib.request

url = 'http://www.hellobi.com'
for i in range(0, 100):
    try:
        file = urllib.request.urlopen(url, timeout=1).read()
        print(len(file))
    except Exception as err:
        print('出现异常')
