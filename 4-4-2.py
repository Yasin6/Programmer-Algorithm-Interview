# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:12:11 2018

@author: Administrator
"""

def  getNum(arr):
    if  arr==None or len(arr)<=0:
        print  "参数不合理"
        return  -1
    a = arr[0]
    b = 1
    lens=len(arr)
    i=1
    while  i <lens:
         a = a ^ arr[i]
         i +=1
    i=2
    while  i <=lens+1:
        b = b ^ i
        i +=1
    return  a^b

if  __name__=="__main__":
    arr=[1, 4, 3, 2, 7, 5]
    print  getNum(arr)
