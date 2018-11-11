# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:09:16 2018

@author: Administrator
"""

def  findDup(array):
    if  None==array:
        return  -1
    lens=len(array)
    index = 0
    i=0
    while  True:
        # 数组中的元素的值只能小于len，否则会越界
        if  array[i]>=lens:
            return  -1
        if  array[index]<0:
            break
        # 访问过，通过变相反数的方法进行标记
        array[index] *= -1 
        # index的后继为array[index]
        index = -1*array[index]
        if  index>=lens:
            print  "数组中有非法数字"
            return  -1
    return  index
