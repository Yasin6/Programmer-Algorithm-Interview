# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:17:07 2018

@author: Administrator
"""

# 判断一个自然数是否是某个数的平方
def  isPower(n):
    if  n<=0:
        print  n+"不是自然数"
        return  False
    i=1
    while  i<n:
        m=i*i
        if  m==n:
            return  True
        elif  m>n:
            return  False
        i +=1
    return  False

if  __name__=="__main__":
    n1=15
    n2=16
    if  isPower(n1):
        print  str(n1)+"是某个自然数的平方"
    else:
        print  str(n1)+"不是某个自然数的平方"
    if  isPower(n2):
        print  str(n2)+"是某个自然数的平方"
    else:
        print  str(n2)+"不是某个自然数的平方"
