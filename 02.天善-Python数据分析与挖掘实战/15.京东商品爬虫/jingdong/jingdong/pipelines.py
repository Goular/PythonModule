# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class JingdongPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="dangdang", charset='utf8')
        title = item['title']
        shop = item['shop']
        shoplink = item['shoplink']
        price = item['price']
        comment = item['comment']
        sql = "insert into goods(title,shop,shoplink,price,comment) values('" + title + "','" + shop + "','" + shoplink + "','" + price + "','" + comment + "')"
        conn.query(sql)
        conn.commit()
        conn.close()
        return item
