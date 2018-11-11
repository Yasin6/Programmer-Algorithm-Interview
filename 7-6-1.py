# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:36:57 2018

@author: Administrator
"""

def  combinationCount(n):
    count=0
    num1=n   	# 1最多的个数
    num2=n/2  	# 2最多的个数
    num5=n/5 	# 5最多的个数
    x=0
    while  x<=num1:
        y=0
        while  y<=num2:
            z=0
            while  z<=num5:
                if  x+2*y+5*z==n: # 满足条件
                    count +=1
                z +=1
            y +=1
        x +=1
    return  count

if  __name__=="__main__": 
    print  combinationCount(100)
