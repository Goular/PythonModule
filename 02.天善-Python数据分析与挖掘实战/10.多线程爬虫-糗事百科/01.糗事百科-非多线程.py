import urllib.request
import re
import urllib.error

headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for i in range(1, 36):
    url = "http://www.qiushibaike.com/8hr/page/" + str(i)
    pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    rsts = re.compile(pat, re.S).findall(pagedata)
    for j in range(0, len(rsts)):
        print("第" + str(i) + "页第" + str(j) + "个段子的内容是：")
        print(rsts[j])