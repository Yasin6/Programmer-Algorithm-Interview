# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:14:28 2018

@author: Administrator
"""

def   minDistance(arr,num1,num2):
    if  arr==None or len(arr)<=0:
        print  "参数不合理"
        return  2**32
    minDis = 2**32   # num1与num2的最小距离
    dist=0
    i=0
    while  i <len(arr):
        if  arr[i] == num1:
            j=0
            while  j < len(arr):
                if  arr[j] == num2:
                    dist=abs(i-j)  # 当前遍历的num1与num2的距离
                    if  dist < minDis:
                        minDis=dist
                j +=1
        i +=1
    return  minDis

if  __name__=="__main__":
    arr=[4, 5, 6, 4, 7, 4, 6, 4, 7, 8, 5, 6, 4, 3, 10, 8]
    num1=4
    num2=8
    print  minDistance(arr,num1,num2)
