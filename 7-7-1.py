# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:37:35 2018

@author: Administrator
"""

def  factorIsOdd(a):
    total =0
    i=1
    while  i<=a:
        if  a%i == 0:
            total +=1
        i +=1
    if  total%2 == 1:
        return  1
    else:
        return  0

def  totalCount(num,n):
    count = 0
    i=0
    while  i<n:
        # //判断因子数是否为奇数，如果是奇数（灯亮），那么加1
        if  factorIsOdd(num[i]) ==1:
            print  "亮着的灯的编号是："+str(num[i])
            count +=1
        i +=1
    return  count
	
if  __name__=="__main__": 
    num =[None] * 100
    i=0
    while  i<100:
        num[i] = i+1
        i +=1
    count = totalCount(num,100)
    print  "最后总共有"+str(count)+"盏灯亮着。"
