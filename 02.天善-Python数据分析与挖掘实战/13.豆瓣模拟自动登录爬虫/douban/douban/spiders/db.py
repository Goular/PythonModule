# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request
class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["douban.com"]
    header={"User-Agent:":"Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)"}
    '''
    start_urls = (
        'http://www.douban.com/',
    )
    '''
    def start_requests(self):
        return [Request("https://accounts.douban.com/login",callback=self.parse,meta={"cookiejar":1})]
    def parse(self, response):
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()
        url="https://accounts.douban.com/login"
        if len(captcha)>0:
            print("此时验证码")
            localpath="F:/天善-Python数据分析与挖掘课程/result/42/captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            print("请查看本地验证码图片并输入验证码")
            captcha_value=input()

            data={
                "form_email":"weisuen007@163.com",
                "form_password":"weijc7789",
                "captcha-solution":captcha_value,
                "redir":"https://www.douban.com/people/151968962/",
            }
        else:
            print("此时没有验证码")
            data={
                "form_email":"weisuen007@163.com",
                "form_password":"weijc7789",
                "redir":"https://www.douban.com/people/151968962/",
            }
        print("登陆中……")
        return [FormRequest.from_response(response,
                                              meta={"cookiejar":response.meta["cookiejar"]},
                                              headers=self.header,
                                              formdata=data,
                                              callback=self.next,
                                              )]

    def next(self,response):
        print("此时已经登陆完成并爬取了个人中心的数据")
        title=response.xpath("/html/head/title/text()").extract()
        note=response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note[0])
