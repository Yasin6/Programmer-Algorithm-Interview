# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:15:11 2018

@author: Administrator
"""

def  maxs(a,b,c):
    maxs = b if  a < b  else  a
    maxs = c if  maxs < c else  maxs
    return  maxs

def  minDistance(a,b,c):
    aLen = len(a)
    bLen = len(b)
    cLen = len(c)
    minDist = maxs(abs(a[0] - b[0]),abs(a[0] - c[0]), abs(b[0] - c[0]))
    dist = 0
    i=0
    while  i < aLen:
        j=0
        while  j < bLen:
            k=0 
            while  k < cLen:
                # 求距离
                dist = maxs(abs(a[i] - b[j]),abs(a[i] - c[k]),abs(b[j] - c[k]))
                # 找出最小距离
                if  minDist > dist:
                    minDist = dist
                k +=1
            j +=1
        i +=1
    return  minDist

if  __name__=="__main__":
    a=[3, 4, 5, 7, 15]
    b=[10, 12, 14, 16, 17]
    c= [20, 21, 23, 24, 37, 30]
    print   "最小距离为："+ str(minDistance(a, b, c))
