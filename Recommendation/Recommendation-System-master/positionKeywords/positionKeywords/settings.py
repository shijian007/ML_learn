# -*- coding: utf-8 -*-

# Scrapy settings for positionKeywords project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'positionKeywords'

SPIDER_MODULES = ['positionKeywords.spiders']
NEWSPIDER_MODULE = 'positionKeywords.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

ITEM_PIPELINES = {
   'positionKeywords.pipelines.PositionkeywordsPipeline': 300,
}
