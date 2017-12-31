import urllib.request
import urllib.error
import re

url = 'http://blog.csdn.net/'
# <a strategy="recommend" href="http://blog.csdn.net/oschina2017/article/details/78929456" target="_blank">
pat = '<a\s+strategy="recommend"\s+href="(.*?)"\s+target="_blank">'
# 获取html页面内容
data = urllib.request.urlopen(url).read()
# 解码
data = data.decode('utf-8', 'ignore')  # 有时候会因为编码的问题的报错需要ignore
rsts = re.compile(pat).findall(data)
print(len(rsts))
for num in range(0, len(rsts)):
    try:
        print(rsts[num])
        urllib.request.urlretrieve(rsts[num], './blog_html/' + str(num) + ".html")
        print('保存成功')
    except Exception as err:
        if hasattr(err, 'code'):
            print(err.code)
        if hasattr(err, 'reason'):
            print(err.reason)
