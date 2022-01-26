# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:04:40 2018

@author: Arvinder Shinh
"""

import pandas as pd
import numpy as np

def transformer(frame, catagoryColumn='tag_category', 
                tagColumn='matched_tag', 
                text='text', 
                shortDescription='preview_text', 
                shortDescriptionLen='200', 
                columnList=['heading','preview_text','timestamp','source_link','html_file','website_name','tag_category','matched_tag'], 
                noTagColumn='other_tags', 
                noTagValue='other'):
    
    catagories = [x for x in frame.columns if x.endswith("tags")]
    dataColumns = [x for x in frame.columns if not x.endswith("tags")] 
    
    frame[noTagColumn]=np.NaN
    
    condition = True
    for catagory in catagories:
           condition = condition & pd.isna(frame[catagory]).values
    
    frame.loc[condition,[noTagColumn]]=noTagValue
    
    catagories.append(noTagColumn)
    
    X, Y = len(frame.index), len(catagories)
    data = {dataColumn : np.tile(np.asarray(frame[dataColumn]), Y) for dataColumn in dataColumns}
    
    data[catagoryColumn] = np.asarray(catagories).repeat(X)
    data[tagColumn] = frame.loc[:, catagories].values.ravel('F')
    
    dataFrame = pd.DataFrame(data)
    dataFrame.dropna(subset=[tagColumn], inplace=True)
    
    dataDict = {}
    j = 0
    for i in range(dataFrame.shape[0]):
             series=dataFrame.iloc[i]
             
             for tag in series[tagColumn].split('#'):
                 if not (tag.strip() == ""):
                    s = series.copy()
                    s[tagColumn] = tag.strip()
                    dataDict[j] = s
                    j = j+1
                    
    pattern='(^.{'+shortDescriptionLen+'})*'
    
    dataFrameTransformed = pd.DataFrame(dataDict).transpose()
    dataFrameTransformed[shortDescription]=dataFrameTransformed[text].str.extract(pattern, expand=False)
    
    return dataFrameTransformed.loc[:,columnList]

dfOriginal = pd.read_csv('C:/Workspace/PythonProject/Django/UrlTagMap/subset_compiled_data.csv')
dfTransformed = transformer(dfOriginal)


dfTransformed.to_csv('C:/Workspace/PythonProject/Django/UrlTagMap/subset_compiled_data_Out.csv',  index=False)

