# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#
# class YellowPipeline(object):
#     def process_item(self, item, spider):
#         return item

import scrapy.pipelines.images
from scrapy.http import Request


class RawFilenameImagePipeline (scrapy.pipelines.images.ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        beg = url.rfind('/') + 1
        end = url.rfind('.')
        if end == -1:
            return f'full/{url[beg:]}.jpg'
        else:
            return f'full/{url[beg:end]}.jpg'