# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:25:07 2018

@author: Administrator
"""

def  MatrixChainOrder (p,i,j):
    if  i == j:
        return  0
    mins = 2**32
    """
通过把括号放在第一个不同的地方来获取最小的代价
每个括号内可以递归地使用相同的方法来计算
    """
    k=i
    while  k<j:
        count = MatrixChainOrder (p, i, k) + \
        MatrixChainOrder (p, k+1, j) + \
        p[i-1]*p[k]*p[j]
        if  count < mins:
            mins = count
        k +=1
    return  mins

if  __name__=="__main__":
    arr=[1, 5, 2, 4, 6]
    n = len(arr)
    print  "最少的乘法次数为 "+str(MatrixChainOrder(arr, 1, n-1))
