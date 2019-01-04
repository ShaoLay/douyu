# -*- coding: utf-8 -*-
import scrapy


class DouyuappSpider(scrapy.Spider):
    name = 'douyuapp'
    allowed_domains = ['www.douyu.com']
    start_urls = ['http://www.douyu.com/']

    def parse(self, response):
        pass
