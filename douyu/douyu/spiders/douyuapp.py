# -*- coding: utf-8 -*-
import json

import scrapy

from douyu.items import DouyuItem


class DouyuappSpider(scrapy.Spider):
    name = 'douyuapp'
    allowed_domains = ['www.douyu.com']
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 返回从json里获取data段数据集合
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuItem()
            item['name'] = each['nichname']
            item['images_urls'] = each['vertical_src']

            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
