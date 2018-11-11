# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:18:40 2018

@author: Administrator
"""

def  isPower(n):
    if  n<1:
        return  False
    m=n&(n-1)
    return  m==0
