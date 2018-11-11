# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:18:09 2018

@author: Administrator
"""

def  maxSubArray(arr):
    if  arr==None or len(arr)<1:
        print  "参数不合法"
        return  
    nAll = arr[0]  # 最大子数组和
    nEnd = arr[0]  # 包含最后一个元素的最大子数组和
    i=1
    while  i<len(arr):
        nEnd =max(nEnd+arr[i],arr[i])
        nAll =max(nEnd,nAll)
        i +=1
    return  nAll 

if  __name__=="__main__":
    arr=[1, -2, 4, 8, -4, 7, -1, -5]
    print  "连续最大和为："+str(maxSubArray(arr))
