# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:21:12 2018

@author: Administrator
"""

def  reverse(arr,start,end):
    while  start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end -=1
	
def  rightShift(arr,k):
    if  arr == None:
        print  "参数不合法"
        return
    lens = len(arr)
    k %= lens
    reverse(arr, 0, lens - k - 1)
    reverse(arr, lens - k, lens - 1)
    reverse(arr, 0, lens - 1)

if  __name__=="__main__":
    k = 4
    arr= [1, 2, 3, 4, 5, 6, 7, 8]
    rightShift(arr, k)
    i=0
    while  i<len(arr):
        print  arr[i],
        i +=1
