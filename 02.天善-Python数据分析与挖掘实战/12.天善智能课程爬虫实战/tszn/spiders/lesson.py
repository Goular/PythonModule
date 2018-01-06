# -*- coding: utf-8 -*-
import scrapy
from tszn.items import TsznItem
from scrapy.http import Request


# 聚焦抓取天善智能的课程
class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['http://edu.hellobi.com/course/120']

    def parse(self, response):
        item = TsznItem()
        item['title'] = response.xpath('/html/body/div[2]/div[1]/div/div[2]/div/h1/text()').extract()
        item['link'] = response.xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/ul/li[1]/a/@href').extract()
        item['stu'] = response.xpath('/html/body/div[2]/div[1]/div/div[2]/div/div[2]/span[2]/text()').extract()
        # print(item['title'])
        # print(item['link'])
        # print(item['stu'])
        yield item
        for i in range(1, 220):
            url = 'http://edu.hellobi.com/course/' + str(i)
            yield Request(url, callback=self.parse)
