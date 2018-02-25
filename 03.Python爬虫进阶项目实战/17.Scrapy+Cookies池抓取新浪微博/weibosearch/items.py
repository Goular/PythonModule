from scrapy import Item, Field


class WeiboItem(Item):
    table_name = 'weibo'
    id = Field()
    url = Field()
    content = Field()
    forward_count = Field()
    comment_count = Field()
    like_count = Field()
    posted_at = Field()
    user = Field()
    crawled_at = Field()
