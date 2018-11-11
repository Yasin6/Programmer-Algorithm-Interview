# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:25:52 2018

@author: Administrator
"""

def  add(n1,n2):
    sums = 0 # 保存不进位相加结果
    carry = 0 # 保存进位值
    while  True:   #判断进位值是否为0 
        sums = n1 ^ n2  #异或代替不进位相加
        carry = (n1 & n2) << 1  # 与操作代替计算进位值
        n1 = sums   
        n2 = carry 
        if  carry==0:
            break
    return  sums

def  sub(a,b):
    return  add(a, add(~b, 1))
