# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:16:28 2018

@author: Administrator
"""

def  findMin(array):
    if  array==None or len(array)<=0:
        print  "输入参数不合理"
        return  0
    mins=2**32
    i =0
    while  i<len(array):
        if  abs(array[i])<abs(mins):
            mins=array[i]
        i +=1
    return  mins

if  __name__=="__main__":
    arr= [-10, -5, -2, 7, 15, 50]
    print  "绝对值最小的数为："+str(findMin(arr))

