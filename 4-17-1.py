# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:23:49 2018

@author: Administrator
"""

def  maxCover(a,L):
    count = 2
    maxCount = 1  # 最长覆盖的点数
    start = 0  # 覆盖坐标的起始位置
    n = len(a)
    i = 0
    j = 1
    while  i < n and j < n:
        while  (j < n) and (a[j] - a[i] <= L):
            j +=1
            count +=1
        j -=1
        count -=1
        if  count>maxCount:
            start = i
            maxCount = count
        i +=1
        j +=1
    print  "覆盖的坐标点: ",
    i=start
    while  i < start + maxCount:
        print  a[i],
        i +=1
    print  '\n'
    return  maxCount

if  __name__=="__main__":
    a= [1, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 25]
    print  "最长覆盖点数:"+ str(maxCover(a, 8))
