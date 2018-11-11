# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:33:46 2018

@author: Administrator
"""

# 获取n的平方根,e为精度要求
def  squareRoot(n,e):
    new_one = n
    last_one = 1.0 #  第一个近似值为1 
    while  new_one - last_one > e: # 直到满足精度要求为止
        new_one = (new_one + last_one)/2 # 求下一个近似值
        last_one = n/new_one
    return  new_one

if  __name__=="__main__":
    n = 50
    e = 0.000001
    print  str(n) + "的平方根为" + str(squareRoot(n,e))
    n=4
    print   str(n) + "的平方根为"+ str(squareRoot(n,e))
