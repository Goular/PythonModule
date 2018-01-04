from scrapy.spider import Spider


class FirstSpider(Spider):
    # 当前爬虫文件类的属性，可以使用first直接访问
    name = 'first'
    # 允许爬取的域名
    allowed_domains = ['baidu.com']
    # 蜘蛛起始地址
    start_urls = ['http://www.baidu.com']

    # 爬取后的回调函数
    def parse(self, response):
        pass