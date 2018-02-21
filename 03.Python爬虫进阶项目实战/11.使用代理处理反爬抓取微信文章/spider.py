from urllib.parse import urlencode
import requests
import pymongo
from lxml.etree import XMLSchemaError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
from config import *

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]
base_url = "http://weixin.sogou.com/weixin?"

proxy = None

headers = {
    'Cookie': 'SUV=006017857920331659FBBE37A9C06758; CXID=CB99002EB39E18A09EEE71BBC5D7F9E3; IPLOC=CN4401; OPENID=6FBB94790FE8A073BA3662A395216A67; wuid=AAE+Y1l0HAAAAAqLE2N/Rg4AGwY=; pgv_pvi=9151333376; m=95C3D5AEBA372255C07D371AE6EF9BBA; sw_uuid=4871306690; sg_uuid=6180462505; dt_ssuid=3911739940; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ssuid=5435298050; usid=XEqpicX1z5y03rUC; GOTO=Af22417-3002; ld=9Zllllllll2zxFISlllllVIZKLYlllllWvl8jlllllGlllll4klll5@@@@@@@@@@; LSTMV=280%2C38; LCLKINT=1597; ad=HZllllllll2BMDGklllllV$wp99lllllWvl8Vkllllylllll9qxlw@@@@@@@@@@@; SUID=163320793765860A59FBC3200003E951; YYID=95C3D5AEBA372255C07D371AE6EF9BBA; ABTEST=0|1519112143|v1; weixinIndexVisited=1; sct=2; JSESSIONID=aaa2a2uk0lPyk-zjVHQfw; ppinf=5|1519211307|1520420907|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo2OkdvdWxhcnxjcnQ6MTA6MTUxOTIxMTMwN3xyZWZuaWNrOjY6R291bGFyfHVzZXJpZDo0NDpvOXQybHVLbE5rTG1sb3Jhb1ZBSXRLRzJodmlvQHdlaXhpbi5zb2h1LmNvbXw; pprdig=bjqzF2nnPQ_kVTuUIh9o_lRyHJgPZhm3DCMVT_5kZLhYprsG3dn8yt0F6VxN2fvjhZiShl7wvRgz4KqvUxgc7lFjSMAGM06DExesBvoQwxB9KZ2kpQ81oAnFB6UFHQTEExGQsbhzmLpKGpr-ApYV75pqBJRgxm-sjgRxI9DD60w; sgid=21-33710095-AVqNUyv3iaakuNfsCRdgUaEE; PHPSESSID=rlag69f6v60maj7a5f3sborvr5; SUIR=25B57061595F3FC5810E623D5AE997DC; SNUID=464ED1C3F8FD9D4EDAA87586F9A88132; ppmdig=1519214676000000eed7c919f575efcf05280168acb2200c',
    'Host': 'weixin.sogou.com',
    'Referer': 'http://weixin.sogou.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}


# 获取代理地址
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError as err:
        return None


def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    if count >= MAX_COUNT:
        print("Tried Too Many Count")
        return None
    try:
        if proxy:
            proxies = {
                'http': "http://" + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            # pass
            print("出现302异常")
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as err:
        print('Error Occurred', err.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    return get_html(url)


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError as err:
        return None


def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('.rich_media_meta_list .rich_media_meta_nickname').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title': title,
            'content': content,
            'date': date,
            'nickname': nickname,
            'wechat': wechat
        }
    except XMLSchemaError as err:
        return None


def save_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved to Mongo', data['title'])
    else:
        print('Saved to Mongo Failed', data['title'])


def main():
    for page in range(1, 101):
        html = get_index(KEYWORD, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)


if __name__ == '__main__':
    main()
