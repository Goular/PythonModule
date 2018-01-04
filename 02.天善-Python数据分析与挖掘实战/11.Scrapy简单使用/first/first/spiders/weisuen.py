# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # pass
        item = FirstItem()
        item['content']=response.xpath('/html/head/title/text()').extract()
        yield item