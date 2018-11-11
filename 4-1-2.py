# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:08:41 2018

@author: Administrator
"""

def  findDup(array):
    if  None==array:
        return  -1
    lens=len(array)
    result = 0
    i=0
    while  i <lens:
        result ^= array[i]
        i +=1
    j=1
    while  j<lens:
        result ^= j
        j +=1
    return  result
