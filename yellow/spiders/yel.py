# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import YellowItem
from scrapy import Request


class YelSpider(scrapy.Spider):
    name = 'yel'
    allowed_domains = ['www.sstt12.com']
    start_urls = ['http://www.sstt12.com/Art/AtrNr/20914.html','http://www.sstt12.com/Art/AtrNr/20915.html']
    url_next = 'http://www.sstt12.com/Art/AtrNr/{}.html'
# hahah
    def parse(self, response):
        get_rs = response.xpath('/html/body/div[6]/div/div[4]/img').extract()
        item = YellowItem()
        # item['referer'] = response.url
        for get_r in get_rs:
            item["image_urls"] = re.findall("http.*jpg", "".join(get_r))
            # print(i)
            # print(type(item["image_urls"]))
            # print("".join(get_r))
            yield item
        # list_11=(20639)
        for i in range(15000, 35000, 100):
            yield Request(self.url_next.format(i), callback=self.parse)

