#coding:utf-8
'''
根据每个职位对应的链接爬取对应的信息(只能爬取一页信息)
'''
import scrapy,json,re,os
from scrapy import Selector
from positionDetails.items import PositiondetailsItem
from bs4 import BeautifulSoup


basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class LagoupositonSpider(scrapy.Spider):
    name = "lagou2"
    allowed_domains = ["*.lagou.com"]
    start_urls = [
        "http://www.lagou.com/"
    ]

    myurl = "http://www.lagou.com/jobs/positionAjax.json?px=new"

    curpage = 0

    # 爬取python
    kd = 'python'

    def start_requests(self):
        return [scrapy.http.FormRequest(self.myurl,
                                        formdata={'pn': str(self.curpage), 'kd': self.kd}, callback=self.parse)]


    def parse(self, response):
        kd = "python"
        positionLink = "http://www.lagou.com/jobs/{}.html"
        jdict = json.loads(response.body_as_unicode())
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        jresult = jposresult["result"]
        self.totalPageCount = jposresult['totalCount'] / 15 + 1

        for each in jresult:
            print "*****************************"
            print positionLink.format(each['positionId'])
            yield scrapy.Request(positionLink.format(each['positionId']), callback=self.parse_detail, meta={'kd': kd},
                                 dont_filter=True)

    # 根据每个职位对应的链接，返回相应的职位信息
    def parse_detail(self, response):
        item = PositiondetailsItem()
        sel = Selector(response)

        try:
            item["kd"] = response.meta['kd']
            item["positionName"] = self.get_text(sel, '//*[@id="job_detail"]/dt/h1/@title')
            item["companyName"] = sel.xpath('//*[@id="container"]/div[2]/dl/dt/a/div/h2/text()').extract()[0].strip()
            item["city"] = sel.xpath('//*[@id="job_detail"]/dd[1]/p[1]/span[2]/text()').extract()[0]
            # item["address"] = sel.xpath('//*[@id="container"]/div[2]/dl/dd/div[1]/text()').extract()[0]
            # industry = sel.xpath('//*[@id="container"]/div[2]/dl/dd/ul[1]/li[1]').extract()[0]
            # item["industry"] = BeautifulSoup(industry).get_text().encode("utf-8").split(' ')[1].strip()
            scale = sel.xpath('//*[@id="container"]/div[2]/dl/dd/ul[1]/li[2]').extract()[0]
            item["scale"] = BeautifulSoup(scale).get_text().encode("utf-8").split(' ')[1].strip()
            # phase = sel.xpath('//*[@id="container"]/div[2]/dl/dd/ul[2]/li').extract()[0]
            # item["phase"] = BeautifulSoup(phase).get_text().encode("utf-8").split(' ')[1].strip()
            item["salary"] = sel.xpath('//*[@id="job_detail"]/dd[1]/p[1]/span[1]/text()').extract()[0]
            item["experience"] = sel.xpath('//*[@id="job_detail"]/dd[1]/p[1]/span[3]/text()').extract()[0]
            item["education"] = sel.xpath('//*[@id="job_detail"]/dd[1]/p[1]/span[4]/text()').extract()[0]
            item["description"] = self.get_text(sel, '//*[@id="job_detail"]/dd[2]')
            item["url"] = response.url
            item["publishedTime"] = sel.xpath('//*[@id="job_detail"]/dd[1]/p[3]/text()').extract()[0][:-8]
            item["tag"] = self.get_text(sel, '//*[@id="job_detail"]/dd[1]/p[2]/text()')

        except Exception, e:
            print e
        yield item

    def get_text(self, sel, path):
        xpath_text = sel.xpath(path).extract()[0]
        text = BeautifulSoup(xpath_text).get_text()
        text = re.sub(r'\n|\r|\t|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\\|"\"|\"', '', text)
        return text


