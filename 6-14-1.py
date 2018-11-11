# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:34:06 2018

@author: Administrator
"""

class  MyXOR:
    def  __init__(self):
        self.BITS=32       
    # 获取x与y的异或的结果
    def  xor(self,x,y):
        res = 0 
        i=self.BITS-1
        while  i>=0:
            # 获取x与y当前的bit值
            b1 = (x & (1 << i))>0
            b2 = (y & (1 << i))>0
            # 只有这两位都是1或0的时候结果为0 
            if  (b1==b2):
                xoredBit = 0
            else: 
                xoredBit = 1
            res <<= 1
            res |= xoredBit
            i -=1
        return  res

if  __name__=="__main__":
    x = 3
    y = 5
    mx=MyXOR()
    print  mx.xor(x, y)

