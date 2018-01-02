import urllib.request
import urllib.parse
import re

# 淘宝依据"关键词"爬取相关的图片(并下载到本地)并下载
param = "篮球"
key = urllib.request.quote(param)
# 该链接仅在火狐下才能抓取到图片地址，而其他浏览器是不能正确捕获到图片，可能需要抓包才能获取图片真正链接
# 爬虫不要为了炫技，换个浏览器简单抓就不用抓包复杂抓，切记！切记！
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

for i in range(1, 2):
    try:
        url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20180101&stats_click=search_radio_all%3A1&js=1&imgfile=&q=' + key + '&suggest=0_1&_input_charset=utf-8&source=suggest&bcoffset=4&p4ppushleft=1%2C48&s=' + str(
            (i * 44)) + '&ntoffset=4'
        pat = 'pic_url":"//(.*?)"'
        url_data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        raw_imgs = re.compile(pat).findall(url_data)
        for j in range(0, len(raw_imgs)):
            fileName = './img/' + str(i) + str(j) + ".jpg"
            urllib.request.urlretrieve("http://" + raw_imgs[j], fileName)
    except Exception as err:
        print(err)
