#coding:utf-8

'''
爬取职位信息，不包括职位的描述详情
'''
import scrapy,json,re,os
from scrapy import Selector
from positionDetails.items import PositiondetailsItem
from bs4 import BeautifulSoup

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class LagoupositonSpider(scrapy.Spider):
    name = "lagou"

    totalPageCount = 0
    curpage = 1
    cur = 0

    keywords = [json.loads(line) for line in open(basedir + '/positionData/KeyWords.json')]
    myurl = "http://www.lagou.com/jobs/positionAjax.json?px=new"

    # 爬取所有的技术类
    # kds = keywords[0][u'技术'][0]
    # kd = kds[0]
    # def start_requests(self):
    #     return [scrapy.http.FormRequest(self.myurl,
    #                                 formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)]

    # 爬取Python
    kd = 'python'
    def start_requests(self):
        return [scrapy.http.FormRequest(self.myurl,
                                    formdata={'pn':str(self.curpage),'kd':self.kd},callback=self.parse)]

    def parse(self, response):

        item = PositiondetailsItem()
        jdict = json.loads(response.body)
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        jresult = jposresult["result"]
        self.totalPageCount = jposresult['totalCount'] /15 + 1

        for each in jresult:
            item['city']=each['city']
            item['companyName'] = each['companyFullName']
            item['companySize'] = each['companySize']
            item['positionType'] = each['jobNature']
            item['positionName'] = each['positionName']
            sal = each['salary']
            sal = sal.split('-')
            print sal
            if len(sal) == 1:
                item['salaryMax'] = int(sal[0][:sal[0].find('k')])
            else:
                item['salaryMax'] = int(sal[1][:sal[1].find('k')])
            item['salaryMin'] = int(sal[0][:sal[0].find('k')])
            item['formatCreatetime'] = each['formatCreateTime']
            item['workYear'] = each['workYear']
            item['companyId'] = each['companyId']
            url = 'www.lagou.com/jobs/'+ str(item['companyId']) + '.html'
            item['link'] = url
            item['keyword'] = self.kd
            yield item


        if self.curpage <= self.totalPageCount:
            self.curpage += 1
            yield scrapy.http.FormRequest(self.myurl,
                                        formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
        # elif self.cur < len(self.kds)-1:
        #     self.curpage = 1
        #     self.totalPageCount = 0
        #     self.cur += 1
        #     self.kd = self.kds[self.cur]
        #     yield scrapy.http.FormRequest(self.myurl,
        #                                 formdata = {'pn': str(self.curpage), 'kd': self.kd},callback=self.parse)
        #
        #
        #
