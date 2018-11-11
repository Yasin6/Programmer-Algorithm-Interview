# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:17:13 2018

@author: Administrator
"""

def  maxSubArray(arr):
    if  arr==None or len(arr)<1:
        print  "参数不合法"
        return  
    ThisSum=0 
    MaxSum=0
    i=0
    while  i<len(arr):
        j=i
        while  j<len(arr):
            ThisSum=0
            k=i
            while  k<j:
                ThisSum +=arr[k]
                k +=1
            if  ThisSum>MaxSum:
                MaxSum=ThisSum            
            j +=1
        i +=1
    return  MaxSum  

if  __name__=="__main__":
    arr=[1, -2, 4, 8, -4, 7, -1, -5]
    print  "连续最大和为："+str(maxSubArray(arr))
