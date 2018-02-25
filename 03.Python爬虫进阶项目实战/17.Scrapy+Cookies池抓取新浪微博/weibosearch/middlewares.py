# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import requests
import json
from scrapy import signals
import logging

from scrapy.exceptions import IgnoreRequest


class WeibosearchSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WeibosearchDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 创建Cookies代理池，并访问中间件
class CookiesMiddleware():
    def __init__(self, cookies_pool_url):
        self.logger = logging.getLogger(__name__)
        self.cookies_pool_url = cookies_pool_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies_pool_url=crawler.settings.get('COOKIES_POOL_URL')
        )

    # 通过随机Cookies池，随机获取cookies的资料
    def _get_random_cookies(self):
        try:
            response = requests.get(url=self.cookies_pool_url)
            if response.status_code == 200:
                return json.loads(response.text)
        except ConnectionError as err:
            return None

    # 执行于请求前
    def process_request(self, request, spider):
        # 获取cookies资料
        # cookies = self._get_random_cookies()
        # # 如果cookies存在，运行下面更改cookies的内容
        # if cookies:
        #     request.cookies = cookies
        #     self.logger.debug('Using Cookies' + json.dumps(cookies))
        # else:
        #     self.logger.debug('No Valid Cookies')

        # 由于我们没有多账号，所以只能进行单一账号的cookies读取
        request.cookies = {
            '_T_WM': '8a6c57d46bce078ac65a74bc84b9d97b',
            'SCF': 'Ag2kd5Eig5CH-ojY4LlUDkJMvClgSnEIJAEULW51tF17eTilzwzS_5QqtI6Idrc5YUoqrVWHONczWb1El7d6mkk.',
            'SUB': '_2A253lDhaDeThGeRP7VoQ8SfLzjiIHXVVd1gSrDV6PUJbkdAKLWXbkW1NUBkq0Af4HEaOTfkhDKY9F-Hyr0WnWuC7',
            'SUHB': '0h1YjjXqCyk4rv'
        }

    # 对反爬虫的转跳和异常进行处理
    def process_response(self, request, response, spider):
        # return response
        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers['location']
                if 'passport' in redirect_url:
                    self.logger.warning('Need Login,Updating Cookies')
                elif 'weibo.cn/security' in redirect_url:
                    self.logger.warning('Account is Locked!')
                request.cookies = self._get_random_cookies()
                return request
            except:
                raise IgnoreRequest
        elif response.status in [414]:
            return request
        else:
            # 没有异常的就直接都进行输出
            return response
