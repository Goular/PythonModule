import urllib.request
import urllib.parse
import urllib.error
import re
import random

# 作业：千图网
# 爬取千图网的指定模块的图片，同时可以根据设定指定下载连续的几页
# http://www.58pic.com/piccate/2-3-68-1.html
# http://www.58pic.com/piccate/2-3-68-2.html
# http://www.58pic.com/piccate/2-3-68-3.html

# 由于img标签的内容太简单，没有特殊性，所以只能延长标签字符串的长度，增加特殊性
# class="thumb-box" target="_blank"><img  src="http://pic.qiantucdn.com/58pic/25/72/38/48W58PICkwS.jpg!qt290"

# 基础地址
url = 'http://www.58pic.com/piccate/2-3-68'
# 模式
pat = '<img.*="(.*?)!qt290"'
# pat = 'class="thumb-box".*?src="(.*?)!qt290"'
# <a class="thumb-box".*?src="(.*?).jpg!

for i in range(1, 10):
    # 组合拼接字符串
    page = str(i)
    real_url = url + '-' + page + ".html"
    print('抓取页面地址:' + real_url)
    # 抓取页面数据
    data = urllib.request.urlopen(real_url).read().decode('utf-8', 'ignore')
    # 正则表达式
    rsts = re.compile(pat).findall(data)
    if len(rsts):
        print('抓取第' + str(i) + '页数据成功')
    results = iter(rsts)
    for index, data in enumerate(results):
        try:
            urllib.request.urlretrieve(data, './img/' + str(i) + '-' + str(index) + ".jpg")
            print('当前打印的是第' + str(i) + '页第' + str(index + 1) + '张图片')
        except urllib.error.URLError as err:
            if hasattr(err, 'code'):
                print(err.code, end='')
            if hasattr(err, 'reason'):
                print(err.reason)
        except Exception as err:
            print(err)
