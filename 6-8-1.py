# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:30:05 2018

@author: Administrator
"""

def  searth(n):
    i=0
    count = 0
    i=1
    while  True:
        if  i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            count +=1
        if  count == n:
            break
        i +=1
    return  i

if  __name__=="__main__":
    print  searth(1500)
