# -*- coding: utf-8 -*-

import os
# Scrapy settings for positionDetails project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'positionDetails'

SPIDER_MODULES = ['positionDetails.spiders']
NEWSPIDER_MODULE = 'positionDetails.spiders'

COOKIES_ENABLED=False

DOWNLOAD_DELAY=3

SPIDER_MIDDLEWARES = {
    'positionDetails.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'positionDetails.middlewares.ProxyMiddleware': 100,

}


ITEM_PIPELINES = {
   'positionDetails.pipelines.PositiondetailsPipeline': 300,
}


