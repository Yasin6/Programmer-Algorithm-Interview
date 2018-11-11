# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:18:25 2018

@author: Administrator
"""

class  Test:
    def  __init__(self ):
        self.begin =0   # 记录最大子数组起始位置
        self.end = 0   # 记录最大子数组结束位置       
    def  maxSubArray(self,arr):
        n=len(arr)
        maxSum = -2**31 # 子数组最大值
        nSum = 0 # 包含子数组最后一位的最大值
        nStart=0 
        i=0
        while  i<n:
            if  nSum < 0:
                nSum = arr[i]
                nStart=i  
            else: 
                nSum += arr[i]
            if  nSum > maxSum:
                maxSum = nSum
                self.begin=nStart
                self.end=i
            i +=1
        return  maxSum   
    def  getBegin(self): return  self.begin
    def  getEnd(self): return  self.end

if  __name__=="__main__":
    t =Test()
    arr=[1, -2, 4, 8, -4, 7, -1, -5]
    print  "连续最大和为："+str(t.maxSubArray(arr))
    print  "最大和对应的数组起始与结束坐标分别为：" + str(t.getBegin())+","+str(t.getEnd())
