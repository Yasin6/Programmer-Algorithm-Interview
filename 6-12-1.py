# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:32:58 2018

@author: Administrator
"""

"""
方法功能：计算一个数的n次方
输入参数：d为底数，n为幂
返回值：  d^n
"""
def  power(d,n):
    if  n==0: return  1
    if  n==1: return  d
    result=1.0
    if  n>0:
        i=1
        while  i<=n:
            result*=d
            i +=1
        return  result
    else:
        i=1
        while  i<=abs(n):
            result=result/d
            i +=1
    return  result

if  __name__=="__main__":
    print  power(2,3)
    print  power(-2,3)
    print  power(2,-3)

