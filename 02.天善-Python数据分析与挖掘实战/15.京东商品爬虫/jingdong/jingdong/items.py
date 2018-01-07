# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    title = scrapy.Field()
    shop = scrapy.Field()
    shoplink = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()
