# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:15:51 2018

@author: Administrator
"""

def  mins(a,b,c):
    mins = a if  a < b  else b
    mins = mins if  mins < c else c
    return  mins

def  maxs(a,b,c):
    maxs = b if  a < b else a
    maxs =c if  maxs < c else maxs
    return  maxs

def  minDistance(a,b,c):
    aLen = len(a)
    bLen = len(b)
    cLen = len(c)
    curDist = 0 
    minsd = 0
    minDist =2 **32
    i=0 # 数组a的下标
    j=0 # 数组b的下标
    k=0 # 数组c的下标
    while  True:
        curDist = maxs(abs(a[i] - b[j]),abs(a[i] - c[k]),abs(b[j] - c[k]))
        if  curDist < minDist:
            minDist = curDist
		# 找出当前遍历到三个数组中的最小值
        minsd = mins(a[i], b[j], c[k])
        if  minsd == a[i]:
            i +=1
            if  i >= aLen:
				break
        elif  minsd == b[j]:
            j +=1
            if  j >= bLen:
                break
        else:
            k +=1
            if  k >= cLen:
                break       
    return  minDist

if  __name__=="__main__":
    a=[3, 4, 5, 7, 15]
    b=[10, 12, 14, 16, 17]
    c= [20, 21, 23, 24, 37, 30]
    print   "最小距离为："+ str(minDistance(a, b, c))
