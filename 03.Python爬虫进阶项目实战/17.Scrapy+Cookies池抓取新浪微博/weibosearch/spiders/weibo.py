# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http.request import Request
from scrapy.http.request.form import FormRequest

from weibosearch.items import WeiboItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    search_url = 'https://weibo.cn/search/mblog'
    max_page = 3

    def start_requests(self):
        keyword = '奥运会'
        url = '{url}?keyword={keyword}'.format(url=self.search_url, keyword=keyword)
        for page in range(self.max_page):
            data = {
                'mp': str(100),
                'page': str(page + 1)
            }
            # 提交Post请求
            yield FormRequest(url=url, callback=self.parse_index, formdata=data)

    def parse_index(self, response):
        # print(response.text)
        # 对页面进行解析
        weibos = response.xpath('//div[@class="c" and contains(@id,"M_")]')
        for weibo in weibos:
            # 判断是否是转发的文章
            is_forward = bool(weibo.xpath('.//span[@class="cmt"]').extract_first())
            if is_forward:
                # 如果是转发的文章
                detail_url = weibo.xpath('.//a[contains(.,"原文评论[")]//@href').extract_first()
            else:
                detail_url = weibo.xpath('.//a[contains(.,"评论[")]//@href').extract_first()
            yield Request(url=detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        id = re.search('comment\/(.*?)\?', response.url).group(1)
        url = response.url
        content = response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract_first()
        print(id, url, content)
        comment_count = response.xpath('//span[@class="pms"]//text()').re_first('评论\[(.*?)\]')
        forward_count = response.xpath('//a[contains(.,"转发[")]//text()').re_first('转发\[(.*?)\]')
        like_count = response.xpath('//a[contains(.,"赞[")]').re_first('赞\[(.*?)\]')
        print(comment_count, forward_count, like_count)
        posted_at = response.xpath('//div[@id="M_"]//span[@class="ct"]//text()').extract_first(default=None)
        user = response.xpath('//div[@id="M_"]/div[1]/a/text()').extract_first(default=None)
        print(posted_at, user)
        weibo_item = WeiboItem()
        for field in weibo_item.fields:
            try:
                weibo_item[field] = eval(field)
            except NameError:
                self.logger.debug('Field is Not Founded' + field)
        yield weibo_item
