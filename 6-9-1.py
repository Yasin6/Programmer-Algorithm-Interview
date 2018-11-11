# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:31:02 2018

@author: Administrator
"""

def  intToBinary(n):
    hexNum = 8 * 8  # 二进制的位数(long占8个字节)
    bit = []
    for  i  in  range(hexNum):
        b=n >> i
        c,d=divmod(b,2)
        bit.append(str(d))
    return  ''.join(bit[::-1])

def  intToHex(s):
    hexs = ""
    remainder = 0
    while  s != 0:
        remainder = s % 16
        if  remainder < 10:
            hexs =str(remainder+ int('0'))+ hexs
        else:
            hexs = str(remainder -10 + ord('A')) + hexs
        s = s >> 4
    return  chr(int(hexs))

if  __name__=="__main__":
    print  "10的二进制输出为："+intToBinary(long(10))
    print  "10的十六进制输出为："+intToHex(long(10))

