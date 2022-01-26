# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:20:32 2019

@author: ArvinderShinh
"""

from HiveTagDataReader import HiveTable
import pandas as pd

url = HiveTable('url_0')

columnName=[ele[0] for ele in url.hqlDescribe()]
WebCrawlingData=pd.DataFrame(url.hqlAll(), columns=columnName)
print(WebCrawlingData['sourcelink'][5])