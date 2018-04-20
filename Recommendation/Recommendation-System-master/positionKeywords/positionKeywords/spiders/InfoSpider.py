#coding:utf-8

#爬取拉勾上所有职位的名称
import scrapy
from scrapy import Selector
from scrapy.spiders import CrawlSpider
#带有默认值的字典
from collections import defaultdict

class KeysSpider(CrawlSpider):
    name = "keywords"
    allowed_domains = ["*.lagou.com"]
    start_urls = [
        "http://www.lagou.com"
    ]

    def parse(self,response):
        sel = Selector(response)
        keys = sel.xpath('//*[@class="menu_main job_hopping"]/h2/text()').extract()
        i = 1
        item = defaultdict(list)
        for key in keys:
            if key.strip() != '':
                print "test"
                print key.strip()
                try:
                    print i
                    item[key.strip()].append(sel.xpath('//*[@class="menu_box"][{}]/div[2]/dl/dd/a/text()'.format(i)).extract())
                    i = i + 1
                    # item["key"].append(key)
                except Exception, e:
                    print e
            else:
                continue
        yield item

