# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:37:18 2018

@author: Administrator
"""

def  combinationCount(n):
    count=0
    m=0
    while  m<=n:
        count +=(m+2)/2
        m +=5
	return  count
