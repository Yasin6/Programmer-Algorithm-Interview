# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:36:16 2018

@author: Administrator
"""

import  random
# 返回0和1的概率都为1/2
def  func1():
    return  int(round(random.random()))

# 返回0的概率为1/4,返回1的概率为3/4
def  func2():
    a1=func1()
    a2=func1()
    tmp=a1
    tmp|=(a2<<1)
    if  tmp==0:
        return  0
    else:
        return  1

if  __name__=="__main__":
    i=0
    while  i<16:
        print  func2(),
        i +=1
    print'\n'
    i=0
    while  i<16:
        print  func2(),
        i +=1
