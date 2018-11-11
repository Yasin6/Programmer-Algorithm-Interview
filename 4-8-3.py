# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:16:12 2018

@author: Administrator
"""

def  mins(a,b,c):
    mins = a if  a < b else b
    mins = mins if mins < c else c
    return  mins

def  minDistance(a,b,c):
    aLen=len(a)
    bLen=len(b)
    cLen=len(c)
    MinSum = 0 # 最小的绝对值和 
    Sum = 0 # 计算三个绝对值的和，与最小值做比较 
    MinOFabc = 0 #  a[i] , b[j] ,c[k]的最小值 
    cnt = 0 # 循环次数统计，最多是l + m + n次 i = 0, j = 0, k = 0 //a,b,c三个数组的下标索引 
    i=j=k=0
    MinSum = (abs(a[i] - b[j]) + abs(a[i] - c[k]) + abs(b[j] - c[k])) / 2 
    cnt=0
    while  cnt <= aLen + bLen + cLen:
        Sum = (abs(a[i] - b[j]) + abs(a[i] - c[k]) + abs(b[j] - c[k])) / 2 
        MinSum = MinSum if  MinSum < Sum else Sum 
        MinOFabc = mins(a[i] ,b[j] ,c[k]) # 找到a[i] ,b[j] ,c[k]的最小值 
        # 判断哪个是最小值，做相应的索引移动 
        if  MinOFabc == a[i]:
            i +=1
            if  i>= aLen:
                break # a[i]最小,移动i 
        if  MinOFabc == b[j]:
            j +=1
            if  j >= bLen:
                break  # b[j]最小,移动j 
        if  MinOFabc == c[k]:
            k +=1
            if  k >= cLen:
                break    # c[k]最小,移动k 
        cnt +=1
    return  MinSum 

if  __name__=="__main__":
    a=[3, 4, 5, 7, 15]
    b=[10, 12, 14, 16, 17]
    c= [20, 21, 23, 24, 37, 30]
    print   "最小距离为："+ str(minDistance(a, b, c))
