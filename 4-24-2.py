# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:28:23 2018

@author: Administrator
"""

def  sort(arr):
    data_count=dict()
    n=len(arr)
    # 把数组中的数放入map中
    i=0
    while  i<n:
        if  str(arr[i]) in data_count:
            data_count[str(arr[i])]= data_count.get(str(arr[i]))+1
        else:
            data_count[str(arr[i])]=1
        i +=1
    index=0
    for  key,value  in  data_count.items():
        i=value
        while  i>0:
            arr[index]=key
            index +=1
            i -=1

if  __name__=="__main__":
    arr =[15, 12, 15, 2, 2, 12, 2, 3, 12, 100, 3, 3]
    sort(arr)
    i=0
    while  i<len(arr):
        print  arr[i],
        i +=1
