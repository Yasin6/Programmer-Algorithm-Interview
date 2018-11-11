# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:11:55 2018

@author: Administrator
"""

def  getNum(arr):
    if  arr==None or len(arr)<=0:
        print  "参数不合理"
        return  -1
    suma = 0
    sumb = 0
    i=0
    while  i <len(arr):
        suma =suma+ arr[i]
        sumb =sumb+i
        i +=1
    sumb=sumb+len(arr)+len(arr)+1
    return  sumb - suma

if  __name__=="__main__":
    arr=[1, 4, 3, 2, 7, 5]
    print  getNum(arr)
