# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:24:14 2018

@author: Administrator
"""

def  swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

# 按照R[i]-O[i]由大到小进行排序
def  bubbleSort(R,O):
    lens = len(R)
    i=0
    while  i<lens-1:
        j=lens-1
        while  j>i:
            if  R[j] - O[j] > R[j - 1] - O[j - 1]:
                swap(R,j,j - 1)
                swap(O,j,j - 1)
            j -=1
        i +=1

def  schedule(R,O,M):
    bubbleSort(R,O)
    left = M  # 剩余可用的空间数
    lens = len(R)
    i=0
    while  i<lens:
        if  left<R[i]: # 剩余的空间无法继续处理第i个请求
            return  False		
        else:   # 剩余的空间能继续处理第i个请求，处理完成后将占用O[i]个空间
            left -= O[i]
        i +=1
    return  True

if  __name__=="__main__":
    R=[10, 15, 23, 20, 6, 9, 7, 16]
    O=[2, 7, 8, 4, 5, 8, 6, 8]
    N = 8
    M = 50
    scheduleResult = schedule(R, O, M)
    if  scheduleResult:
        print  "按照如下请求序列可以完成："
        i=0
        while  i<N:
            print  str(R[i])+","+str(O[i])+"  ",
            i +=1
    else:
        print  "无法完成调度"

