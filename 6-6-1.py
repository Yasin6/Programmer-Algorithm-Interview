# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:28:35 2018

@author: Administrator
"""

def  zeroCount(n):
    count = 0  
    while  n > 0:
        n = n/5  
        count += n  
    return  count  

if  __name__=="__main__":
    print  "1024!末尾0的个数为："+str(zeroCount(1024))
