# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:24:32 2018

@author: Administrator
"""

def  calculate(a,b):
    b[0] = 1
    N = len(a)
    i=1
    while  i<N:
        b[i] = b[i - 1] * a[i - 1]  # 正向计算乘积
        i +=1
    b[0] = a[N - 1]
    i=N-2
    while  i>=1:
        b[i] *= b[0]
        b[0] *= a[i]    # 逆向计算乘积
        i -=1

if  __name__=="__main__":
    a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b =[None]*len(a)
    calculate(a, b)
    i=0
    while  i<len(b):
        print  b[i],	
        i +=1
