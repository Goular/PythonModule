import urllib.request
import urllib.error
import re

headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
comid = '6213300956044005383'
url = 'https://video.coral.qq.com/filmreviewr/c/upcomment/g7jpq0qd0k8xdca?callback=jQuery112408660686604854908_1514996004220&reqnum=3&commentid=' + comid
for i in range(0, 100):
    data = urllib.request.urlopen(url).read().decode('utf-8')
    # 获取的是下一页的内容
    pat = '"last":"(.*?)"'
    nextid = re.compile(pat).findall(data)[0]
    patcom = '"content":"(.*?)",'
    comdata = re.compile(patcom).findall(data)
    for j in range(0,len(comdata)):
        print("------第" + str(i) + str(j) + "条评论内容是:")
        print(eval('u"' + comdata[j] + '"'))
    url = 'https://video.coral.qq.com/filmreviewr/c/upcomment/g7jpq0qd0k8xdca?callback=jQuery112408660686604854908_1514996004220&reqnum=3&commentid=' + nextid