# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Spider, Request

from zhihuusers.items import UserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']

    # 设定首次搜索的用户(一般选择的是大V)
    start_user = 'excited-vczh'

    # 获取用户资料
    user_url = "https://www.zhihu.com/api/v4/members/{user}?include={include}"
    user_query = "locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,columns_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_bind_phone,is_force_renamed,is_bind_sina,is_privacy_protected,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics"

    # 获取用户的关注者列表
    follow_url = "https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}"
    follow_query = "data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics"

    # 获取用户的粉丝列表
    followers_url = "https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}"
    followers_query = "data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics"

    def start_requests(self):
        # 获取用户资料
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)
        # 获取关注者
        yield Request(self.follow_url.format(user=self.start_user, include=self.follow_query, offset=0, limit=20),
                      callback=self.parse_follows)
        # 获取粉丝列表
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20),
                      callback=self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        # 将JSON转为对象并赋值到Item对象
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        # 由于下面的 parse_follows 是一个人的关注者，所以我们需要根据搜索到的关键人，继续搜索当前的人的被关注者
        # 这个可以保证一直可以搜索当前用户关注的人
        yield Request(
            self.follow_url.format(user=result.get('url_token'), include=self.follow_query, offset=0, limit=20),
            callback=self.parse_follows)
        # 获取当前用户的粉丝
        yield Request(
            self.followers_url.format(user=result.get('url_token'), include=self.followers_query, offset=0, limit=20),
            callback=self.parse_followers)

    # 获取关注的人
    def parse_follows(self, response):
        results = json.loads(response.text)

        # 获取用户的内容，同时将Request添加到新的Request
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        # 获取下一页的内容，同时添加新的请求
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(url=next_page, callback=self.parse_follows)

    # 获取用户粉丝
    def parse_followers(self, response):
        results = json.loads(response.text)

        # 获取用户的内容，同时将Request添加到新的Request
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        # 获取下一页的内容，同时添加新的请求
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(url=next_page, callback=self.parse_followers)
