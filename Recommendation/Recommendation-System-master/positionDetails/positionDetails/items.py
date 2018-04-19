# -*- coding: utf-8 -*-

from scrapy import Item,Field

class PositiondetailsItem(Item):

    #关键字
    kd = Field()
    #职位名称
    positionName = Field()
    #城市
    city = Field()
    #公司
    companyName = Field()
    #薪资
    salary = Field()
    #经验
    experience = Field()
    #教育
    education = Field()
    #链接
    url = Field()
    #规模
    scale = Field()
    #发布时间
    publishedTime = Field()
    #描述
    description = Field()
    #职位诱惑
    tag = Field()


    # #lagou
    # positionName = Field()
    # city = Field()
    # companyName = Field()
    # companySize = Field()
    # positionType = Field()
    # salaryMax = Field()
    # salaryMin = Field()
    # workYear = Field()
    # keyword = Field()
    # formatCreatetime = Field()
    # companyId = Field()
    # link = Field()



