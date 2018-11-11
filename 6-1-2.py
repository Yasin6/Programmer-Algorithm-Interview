# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:17:34 2018

@author: Administrator
"""

def  isPower(n):
    low=1
    high=n
    while  low<high:
        mid=(low+high)/2
        power=mid*mid
        # 接着在1～mid-1区间查找
        if  power>n:
            high=mid-1
        # 接着在mid+1到n区间内查找
        elif  power<n:
            low=mid+1
        else:
            return  True
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
