# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:31:23 2018

@author: Administrator
"""

# 判断n二进制码中1的个数
def  countOne(n):
    count =0  # 用来计数
    while  n >0:
        if  (n &1) ==1: # 判断最后一位是否为1
            count +=1 
        n >>=1  # 移位丢掉最后一位
    return  count

if  __name__=="__main__":
    print  countOne(7)
    print  countOne(8)
