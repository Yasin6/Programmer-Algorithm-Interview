# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:10:00 2018

@author: Administrator
"""

def  findDup(array,num):
    s=set()
    if  None==array:
        return  s
    lens=len(array)
    index = array[0]
    num=num-1
    while  True:
        if  array[index]<0:
             num -=1
             array[index] = lens - num
             s.add(index)
        if  num == 0:
            return  s
        array[index] *= -1
        index = array[index] * (-1) 
	
if  __name__=="__main__":
    array=[1,2,3,3,3,4,5,5,5,5,6]
    num=6
    s=findDup(array,num)
    for  i  in  s:
        print  i,

