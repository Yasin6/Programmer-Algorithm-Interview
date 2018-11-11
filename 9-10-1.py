# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:41:22 2018

@author: Administrator
"""

import  heapq

def  getTop(data):
    rowSize = len(data)
    columnSize = len(data[0])
    result3 = [None]* columnSize
    # 保持一个最小堆，这个堆存放来自20个数组的最小数
    heap=[]
    i=0
    while  i < rowSize:
        arr=(None,None,None)#数组设置三个变量，分别为数值，数值来源的数组，数值在数组中的次序index 
        arr=(-data[i][0],i,0)
        heapq.heappush(heap,arr)
        i +=1
    num = 0
    while  num < columnSize:
        # 删除顶点元素
        d = heapq.heappop(heap)
        result3[num] = -d[0]
        num +=1
        if  (num >= columnSize):
            break
        # 将 value 置为该数原数组里的下一个数
        arr=(-data[d[1]][d[2] + 1],d[1],d[2] + 1)
        heapq.heappush(heap,arr)
    return  result3

if  __name__=="__main__": 
    data =[[29, 17, 14, 2, 1],[19, 17, 16, 15, 6],[30, 25, 20, 14, 5]]
    print  getTop(data)
