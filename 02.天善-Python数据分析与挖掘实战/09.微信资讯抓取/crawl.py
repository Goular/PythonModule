# http://weixin.sogou.com/
import re
import urllib.request
import time
import urllib.error
import urllib.request


# 自定义函数，功能为使用代理服务器爬一个网址
def use_proxy(proxy_addr, url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        proxy= urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read().decode('utf-8','ignore')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常，延时1秒执行
        time.sleep(1)


# 设置关键词
key = "Python"
# 设置代理服务器，该代理服务器有可能失效，读者需要换成新的有效代理服务器
proxy = "60.168.52.103:9999"
# 爬多少页
for i in range(0, 10):
    key = urllib.request.quote(key)
    thispageurl = "http://weixin.sogou.com/weixin?type=2&query=" + key + "&page=" + str(i)
    # a="http://blog.csdn.net"
    thispagedata = use_proxy(proxy, thispageurl)
    print(thispagedata)
    print(len(str(thispagedata)))
    pat1 = '<a href="(.*?)"'
    rs1 = re.compile(pat1, re.S).findall(str(thispagedata))
    if (len(rs1) == 0):
        print("此次（" + str(i) + "页）没成功")
        continue
    for j in range(0, len(rs1)):
        thisurl = rs1[j]
        thisurl = thisurl.replace("amp;", "")
        file = "F:/天善-Python数据分析与挖掘课程/result/32/第" + str(i) + "页第" + str(j) + "篇文章.html"
        thisdata = use_proxy(proxy, thisurl)
        try:
            fh = open(file, "wb")
            fh.write(thisdata)
            fh.close()
            print("第" + str(i) + "页第" + str(j) + "篇文章成功")
        except Exception as e:
            print(e)
            print("第" + str(i) + "页第" + str(j) + "篇文章失败")
