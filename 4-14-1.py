# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:20:02 2018

@author: Administrator
"""

def  getAllSubset(array,mask,c):
    length=len(array)
    if  length == c:
        print  "{",
        i=0
        while  i<length:
            if  mask[i] ==1:
                print  array[i],
            i +=1
        print  "}"
    else:
        mask[c] = 1
        getAllSubset(array, mask, c + 1)
        mask[c] = 0
        getAllSubset(array, mask, c + 1)

if  __name__=="__main__":
    array = ['a', 'b', 'c']
    mask =[0,0,0]
    getAllSubset(array, mask, 0)
