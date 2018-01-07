# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request


class DoubanautoSpider(scrapy.Spider):
    name = 'doubanauto'
    allowed_domains = ['douban.com']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}

    # start_urls = ['http://douban.com/']

    def start_requests(self):
        return [Request('https://accounts.douban.com/login', headers=self.header, callback=self.parse,
                        meta={'cookiejar': 1})]

    def parse(self, response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        url = 'https://accounts.douban.com/login'
        if len(captcha) > 0:
            print('此时验证码')
            print(url)
            localpath = './captcha.png'
            urllib.request.urlretrieve(captcha[0], localpath)
            print('请查看本地图片验证码并输入验证码')
            captcha_value = input()
            data = {
                "form_email": "zhaojt_exam@126.com",
                "form_password": "zhao307161",
                "captcha-solution": captcha_value,
                'redir': 'https://www.douban.com/people/172153435/'
            }
        else:
            print('此时没有验证码')
            data = {
                "form_email": "zhaojt_exam@126.com",
                "form_password": "zhao307161",
                'redir': 'https://www.douban.com/people/172153435/'
            }
        print('登录中......')
        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,
                                          )]

    def next(self, response):
        print('此时已经登陆完成并爬取了个人中心的数据')
        title = response.xpath("/html/head/title/text()").extract()
        note = response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note[0])
