# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:14:44 2019

@author: ArvinderShinh
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
   
    
    def hqlDescribe(self):
        with self.hiveCursor() as cursor:
            sql="DESCRIBE "+self.table
            cursor.execute(sql)
            return cursor.fetchall()
    
    def hqlAll(self):
        with self.hiveCursor() as cursor:
            sql="SELECT * FROM "+self.table
            cursor.execute(sql)
            return cursor.fetchall()
        
#+" LIMIT 2"
# sql="SELECT DISTINCT(catagory) FROM "+self.table
# sql="SELECT catagory FROM url GROUP BY catagory"     
# sql="SELECT "+columnName+", COUNT(*) FROM "+self.table+" GROUP BY "+columnName        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            

        
