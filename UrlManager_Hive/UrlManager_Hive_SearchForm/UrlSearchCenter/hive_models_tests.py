# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:56:49 2018

@author: Arvinder Shinh
"""

from hive_models import HiveTable

url = HiveTable('url_0')
#print(url.hqlFilter(tag='delhi'))
#print(url.hqlGet(id=67))
print(url.hqlGroupByCaTag('catagory'))