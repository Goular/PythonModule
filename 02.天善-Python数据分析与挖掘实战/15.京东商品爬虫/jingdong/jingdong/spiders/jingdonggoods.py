# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jingdong.items import JingdongItem
import re
import urllib.request
import urllib


class JingdonggoodsSpider(CrawlSpider):
    name = 'jingdonggoods'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            item = JingdongItem()
            thisUrl = response.url
            pat = 'item.jd.com/(.*?).html'
            x = re.search(pat, thisUrl)
            if x:
                thisid = re.compile(pat).findall(thisUrl)[0]
                # print(thisUrl)
                # print(thisid)
                title = response.xpath('//html/head/title/text()').extract()
                shop = response.xpath("//*[@id='popbox']/div/div[1]/h3/a/text()").extract()
                shoplink = response.xpath("//*[@id='popbox']/div/div[1]/h3/a/@href").extract()
                # print(title)
                # print(shop)
                # print(shoplink)
                priceUrl = "https://p.3.cn/prices/mgets?callback=jQuery6964855&type=1&area=1&pdtk=&pduid=50528027&pdpin=&pin=null&pdbp=0&ext=11000000&source=item-pc&skuIds=J_" + thisid
                commentUrl = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1463&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1&productId=" + thisid
                # print(priceUrl)
                # print(commentUrl)
                priceData = urllib.request.urlopen(priceUrl).read().decode('utf-8', 'ignore')
                commentData = urllib.request.urlopen(commentUrl).read().decode('utf-8', 'ignore')
                pricePat = '"p":"(.*?)"'
                commentPat = '"goodRateShow":(.*?),'
                price = re.compile(pricePat).findall(priceData)
                comment = re.compile(commentPat).findall(commentData)
                # print(price)
                # print(comment)
                # print('')
                if len(title) and len(shop) and len(shoplink) and len(price) and len(comment):
                    item['title'] = title[0]
                    item['shop'] = shop[0]
                    item['shoplink'] = shoplink[0]
                    item['price'] = price[0]
                    item['comment'] = comment[0]
                else:
                    pass
            else:
                pass
            return item
        except Exception as err:
            print(err)
