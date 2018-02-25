# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import pymongo
from weibosearch.items import WeiboItem
import re


class WeiboPipeline(object):
    # 这个时间处理在编码方面有异常,可能是我们的windows系统的bug，所以我暂时不考虑了
    def parse_time(self, datetime):
        if re.match('\d+月\d+日', datetime):
            try:
                datetime = time.strftime('%Y年', time.localtime()) + datetime
            except Exception as err:
                print(err)
        if re.match('\d+分钟前', datetime):
            try:
                minute = re.match('(\d+)', datetime).group(1)
                datetime = time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time() - float(minute) * 60))
            except Exception as err:
                print(err)
        if re.match('今天.*', datetime):
            try:
                datetime = re.match('今天(.*)', datetime).group(1).strip()
                datetime = time.strftime('%Y年%m月%d日', time.localtime()) + ' ' + datetime
            except Exception as err:
                print(err)
        return datetime

    def process_item(self, item, spider):
        if isinstance(item, WeiboItem):
            if item.get('content'):
                item['content'] = item['content'].lstrip(":").strip()
            if item.get('posted_at'):
                item['posted_at'] = item['posted_at'].strip()
                item['posted_at'] = self.parse_time(item['posted_at'])
            print(item)
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 使用update方法可以做简单的爬虫
        self.db[item.table_name].update({'id': item['id']}, {'$set': item}, True)
        return item
