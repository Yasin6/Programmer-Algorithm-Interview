# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:31:44 2018

@author: Administrator
"""

def  countOne(n):
    count =0   # 用来计数
    while  n >0:
        if  n!=0: # 判断最后一位是否为1
            n=n&(n-1)
        count +=1 
    return  count 

if  __name__=="__main__":
    print  countOne(7)
    print  countOne(8)
