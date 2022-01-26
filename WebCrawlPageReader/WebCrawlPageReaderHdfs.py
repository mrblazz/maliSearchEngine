# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:47:52 2019

@author: ArvinderShinh
"""
import subprocess 

#cat = subprocess.Popen(["hadoop", "fs", "-cat", "/path/to/myfile"], stdout=subprocess.PIPE)
#for line in cat.stdout:
#    print line
    
#proc = subprocess.Popen(["hadoop", "fs", "-cat", "/UrlSearchCenter/Arvinder.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc = subprocess.Popen(['hadoop', 'fs', '-ls', '/UrlSearchCenter'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
s_output, s_err = proc.communicate()
s_return =  proc.returncode

print(s_output)




