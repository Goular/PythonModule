# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    # custom_settings = {
    #     'DEFAULT_REQUEST_HEADERS': {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #         'Accept-Language': 'en',
    #     }
    # }

    def __init__(self, mongo_uri, mongo_db, *args, **kwargs):
        super(ZhihuSpider, self).__init__(*args, **kwargs)
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def parse(self, response):
        pass
