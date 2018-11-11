# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:33:22 2018

@author: Administrator
"""

def  power(d,n):
    if  n==0: return  1  
    if  n==1:return  d 
    tmp=power(d,abs(n)/2)+0.0
    #print  tmp
    if  n>0:
        if  n%2==1: # n为奇数
            return  tmp*tmp*d 
        else:  # n为偶数
            return  tmp*tmp  
    else:
        if  n%2==1:
            print  1/(tmp*tmp*d)
            return  1/(tmp*tmp*d)  
        else:
            return  1/(tmp*tmp)  
