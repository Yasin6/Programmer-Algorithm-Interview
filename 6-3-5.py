# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:24:16 2018

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

def  multi (a,b):
    neg = (a > 0) ^ (b > 0) # 结果的正负数标识
    # 首先计算两个正数相乘的结果，最后根据neg确定结果的正负
    if  b<0:
        b=add(~b, 1) # -b
    if  a<0:
        a=add(~a, 1) # -a
    result = 0
    # key:1向左移位后的值，value:移位的次数即位置编号
    bit_position=dict()
    # 计算出1向左移动（0,1,2...31）位的值
    i=0
    while  i<32:
        bit_position[1 << i]=i
    while  b > 0:
        # 计算出最后一位1的位置编号
        position = bit_position[b & ~(b - 1)]  
        result += (a << position)
        b &= b - 1 # 去掉最后一位1
    if  neg:
        result = add(~result, 1)
    return  result
