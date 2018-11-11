# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:19:03 2018

@author: Administrator
"""

# 方法功能：计算两个自然数的除法  
def  divide(m,n):
    print  str(m)+"除以"+str(n),
    res = 0  
    remain = m
    # 被除数减除数，直到相减结果小于除数为止
    while  m>n:
        m=m-n
        res+=1
    remain=m 
    print  "商为："+str(res)+" 余数："+str(remain)

if  __name__=="__main__":
    m = 14  
    n = 4  
    divide(m,n)  

