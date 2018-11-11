# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:26:10 2018

@author: Administrator
"""

def  MatrixChainOrder (p,n):
    cost =[([None]*n)  for  i  in  range(n)]
    i=1
    while  i<n:
         cost[i][i] = 0
         i +=1
    cLen=2
    while  cLen<n:
         i=1
         while  i<n-cLen+1:
             j = i+cLen-1
             cost[i][j] = 2**31
             k=i
             while  k<=j-1:
                 q = cost[i][k] + cost[k+1][j] + p[i-1]*p[k]*p[j]
                 if  (q < cost[i][j]):
                     cost[i][j] = q
                 k +=1
             i +=1
         cLen +=1     
    return  cost[1][n-1]

if  __name__=="__main__":
    arr= [1, 5, 2, 4, 6]
    n = len(arr)
    print  "最少的乘法次数为 "+str(MatrixChainOrder (arr, n))
