# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 00:39:27 2018

@author: Arvinder Shinh
"""

import pandas as pd
#import re

#def urlDesc(url):
#    urlSplit=url.split('/')
#    desc_re=re.search(r"^(.*)-[0-9]*[.]html$", urlSplit[-1])
#    desc=desc_re.group(1).replace('-', ' ')
#    return desc

def pageGenerator(frame):
    
    folderLoc='C:/Workspace/PythonProject/Django/UrlPages/HtmlPages/'

    for i in range(frame.shape[0]):
        with open(folderLoc+frame.loc[i,'html_file'], mode='w', encoding = 'utf-8') as f:
            f.write('<div>')
            f.write('<div>')
            f.write('<h2>')
            f.write(str(frame.loc[i,'heading']))
            f.write('</h2>')
            f.write('</div>')
            f.write('<div>')
            f.write(str(frame.loc[i,'text']))
            f.write('</div>')
            f.write('</div>')
            
    return frame.shape[0]

df = pd.read_csv('C:/Workspace/PythonProject/Django/UrlPages/subset_compiled_data.csv')
print(pageGenerator(df))

