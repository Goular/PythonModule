# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 设置爬取的内容
class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    # 创建了容器不一定要用，但是要用爬虫容器就需要定义Field
    content = scrapy.Field()
    logo = scrapy.Field()
