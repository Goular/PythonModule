# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsznPipeline(object):
    def __init__(self):
        self.fh = open('f:/1.txt','wb')
    def process_item(self, item, spider):
        print(item['title'])
        print(item['link'])
        print(item['stu'])
        self.fh.write(item["title"][0]+"\n"+item["link"][0]+"\n"+item["stu"][0]+"\n"+"--------"+"\n")
        return item
    def close_spider(self):
        self.fh.close()