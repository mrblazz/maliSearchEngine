# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:38:50 2018

@author: Arvinder Shinh
"""

from pyhive import hive

class HiveTable:
    def __init__(self, table, host='localhost', port='10000', database='arvindershinh', auth='NOSASL'):
        self.table = table
        self.host = host
        self.port = port
        self.database = database
        self.auth = auth
        
        
    def hiveCursor(self):
       cursor = hive.connect(host=self.host, port=self.port, database=self.database, auth=self.auth).cursor()
       return cursor
   
    def hqlFilter(self,**args):
        condition_list=list(args.items())
        column, value = condition_list[0]
        
        condition = column+"="+"'"+str(value)+"'"
        for column, value in condition_list[1:]:
            condition = condition+" AND "+column+"="+"'"+str(value)+"'"
   
        with self.hiveCursor() as cursor:
            sql="SELECT * FROM "+self.table+" WHERE "+condition
            cursor.execute(sql)
            return cursor.fetchall()
        
    def hqlGet(self,**args):
        condition_list=list(args.items())
        column, value = condition_list[0]
        
        condition = column+"="+"'"+str(value)+"'"
        for column, value in condition_list[1:]:
            condition = condition+" AND "+column+"="+"'"+str(value)+"'"
       
        with self.hiveCursor() as cursor:
            sql="SELECT * FROM "+self.table+" WHERE "+condition
            cursor.execute(sql)
            return cursor.fetchone()
        
    def hqlAll(self):
        with self.hiveCursor() as cursor:
            sql="SELECT * FROM "+self.table
            cursor.execute(sql)
            return cursor.fetchall()
        
    def hqlGroupByCaTag(self):
        with self.hiveCursor() as cursor:
            sql="SELECT tag_category, matched_tag, COUNT(matched_tag) as tag_count FROM "+self.table+" GROUP BY tag_category, matched_tag"
            cursor.execute(sql)
            return cursor.fetchall()

        

# sql="SELECT DISTINCT(catagory) FROM "+self.table
# sql="SELECT catagory FROM url GROUP BY catagory"     
# sql="SELECT "+columnName+", COUNT(*) FROM "+self.table+" GROUP BY "+columnName        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            

        