# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def process_item(self, item, spider):
        # item必须是item.py文件所定义的
        # print(item['content'])
        for i in range(0, len(item['content'])):
            print(item['content'][i])
            print(item['link'][i])
        return item
