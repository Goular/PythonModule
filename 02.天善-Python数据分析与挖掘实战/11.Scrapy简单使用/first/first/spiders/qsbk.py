# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem


# 糗事百科的基本模板爬虫
class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        it = FristItem()
        it['content'] = response.xpath("//div[@class='content']/span/text()").extract()
        it['link'] = response.xpath("//a[@class='contentHerf']/@href").extract()
        yield it
