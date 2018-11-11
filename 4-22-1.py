# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:26:51 2018

@author: Administrator
"""

def  findCommon(ar1,ar2,ar3):
    i = 0
    j = 0
    k = 0
    n1=len(ar1)
    n2=len(ar2)
    n3=len(ar3)
    # 遍历三个数组
    while  i < n1 and j < n2 and k < n3:
        # 找到了公共元素
        if  ar1[i] == ar2[j] and ar2[j] == ar3[k]:
            print  ar1[i],   
            i +=1
            j +=1
            k +=1
        # ar[i]不可能是公共元素
        elif  ar1[i] < ar2[j]:
            i +=1
        # ar2[j]不可能是公共元素
        elif  ar2[j] < ar3[k]:
            j +=1
        # ar3[k]不可能是公共元素
        else:
            k +=1

if  __name__=="__main__":
    ar1=[2, 5, 12, 20, 45, 85]
    ar2=[16, 19, 20, 85, 200]
    ar3=[3, 4, 15, 20, 39, 72, 85, 190]
    findCommon(ar1, ar2, ar3)
