# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:11:36 2018

@author: Administrator
"""

def  swap(arr,low,high):
    # 交换数组low到high的内容
    while  low<high:
        tmp = arr[low]
        arr[low] = arr[high]
        arr[high] = tmp
        low +=1
        high -=1

def  rotateArr(arr,div):
    if  None==arr or div<0 or div>=len(arr):
        print  "参数不合法"
        return
    # 不需要旋转
    if  div==0 or div== len(arr)-1:
        return
    # 交换第一个子数组的内容
    swap(arr, 0, div)
    # 交换第二个子数组的内容
    swap(arr, div + 1, len(arr) - 1)
    # 交换整个数组的元素
    swap(arr, 0, len(arr) - 1)

if  __name__=="__main__":
    arr=[1, 2, 3, 4, 5]
    rotateArr(arr, 2)
    i=0
    while  i<len(arr):
        print  arr[i],
        i +=1
