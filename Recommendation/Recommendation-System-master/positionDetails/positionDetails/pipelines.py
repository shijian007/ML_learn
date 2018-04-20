# -*- coding: utf-8 -*-


import json,os,logging
import codecs

basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class PositiondetailsPipeline(object):
    #保存信息
    def __init__(self):
        self.file = codecs.open(basedir + '/positionData/0830.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))
        return item

