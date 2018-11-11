# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:30:44 2018

@author: Administrator
"""

def  searth(n):
    a=[0,2,3,4,5,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30]
    ret=(n/22)*30+a[n%22]
    return  ret
