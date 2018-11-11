# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:18:16 2018

@author: Administrator
"""

# 判断n能否表示成2的n次方 
def  isPower(n):
    if  n<1:
        return  False
    i=1
    while  i<=n:
        if  i==n:
            return  True
        i<<=1
    return  False

if  __name__=="__main__":
    if  isPower(8):
        print  "8能表示成2的n次方"
    else:
        print  "8不能表示成2的n次方"
    if  isPower(9):
        print  "9能表示成2的n次方"
    else:
        print  "9不能表示成2的n次方"

