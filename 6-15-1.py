# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:34:28 2018

@author: Administrator
"""

def  prints(n):
    if(n > 0):
        prints(n-1)
        print  str(n),

if  __name__=="__main__":
    prints(100)

