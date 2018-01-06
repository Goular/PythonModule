# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsbk.items import QsbkItem
from scrapy.http import Request


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/']

    # 这个rules为指定自动爬虫的规律
    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )

    # 首次是模拟浏览器获取，但是第二次不执行，所以需要在setting.py中设置User-Agent
    def start_requests(self):
        ua = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield Request('https://www.qiushibaike.com/', headers=ua)

    # 由于段子的首页与详情页的规则是不一样的所以我们需要修改内容
    def parse_item(self, response):
        i = {}
        i["content"] = response.xpath("//div[@class='content']/text()").extract()
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        print(i['content'])
        print(i['link'])
        print('')
        return i
