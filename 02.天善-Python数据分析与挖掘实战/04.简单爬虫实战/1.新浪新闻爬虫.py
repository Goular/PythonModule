import urllib.request
import urllib.error
import re

url = 'http://news.sina.com.cn'
# href="http://news.sina.com.cn/c/nd/2017-12-31/doc-ifyqcwaq6265539.shtml"
pat = 'href="(http://news.sina.com.cn/.*?\.shtml)"'
# 获取html页面内容
data = urllib.request.urlopen(url).read()
# 解码
data = data.decode('utf-8')
rsts = re.compile(pat).findall(data)
print(len(rsts))
for num in range(0, len(rsts)):
    try:
        urllib.request.urlretrieve(rsts[num], './sina_html/' + str(num) + ".html")
        print('保存成功')
    except urllib.error.URLError as err:
        if hasattr(err, 'code'):
            print(err.code)
        if hasattr(err, 'reason'):
            print(err.reason)
