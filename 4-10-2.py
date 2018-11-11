# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:17:33 2018

@author: Administrator
"""

def  maxSubArray(arr):
    if  arr==None or len(arr)<1:
        print  "参数不合法"
        return  
    maxSum = -2**31
    i=0
    while  i<len(arr):
        sums = 0
        j=i
        while  j<len(arr):
            sums += arr[j]
            if  sums > maxSum:
                maxSum = sums
            j +=1
        i +=1
    return  maxSum

if  __name__=="__main__":
    arr=[1, -2, 4, 8, -4, 7, -1, -5]
    print  "连续最大和为："+str(maxSubArray(arr))   
