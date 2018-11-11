# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:13:17 2018

@author: Administrator
"""

def  getMinPath(arr,i,j):
    # 倒着走到了第一个结点，递归结束
    if  i == 0 and j == 0:
        return  arr[i][j]
    # 选取两条可能路径上的最小值
    elif  i > 0 and j > 0:
        return  arr[i][j] + \
    min(getMinPath(arr, i - 1, j), getMinPath(arr, i, j - 1))
    # 下面两个条件只可选择一个
    elif  i > 0 and j == 0:
        return  arr[i][j] + getMinPath(arr, i - 1, j)
		#j > 0 && i = = 0
    else: 
        return  arr[i][j] + getMinPath(arr, i, j - 1)

def  getMinPath2(arr):
    if  arr == None or len(arr) ==0:
        return  0 
    return  getMinPath(arr,len(arr)-1,len(arr[0])-1)

if  __name__=="__main__":
    arr =[[1, 4, 3],[8, 7, 5],[2, 1, 5]] 
    print  getMinPath2(arr)

