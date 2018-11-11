# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:28:10 2018

@author: Administrator
"""

import  random

# 产生的随机数是整数1-7的均匀分布
def  rand7():
    return  int(random.uniform(1,7))

# 产生的随机数是整数1-10的均匀分布
def  rand10():
    x = 0
    while  True:
        x= (rand7()-1)*7 + rand7()
        if  x<=40:
            break
    return  x % 10 + 1

if  __name__=="__main__":
    i=0
    while  i!=10:
        print  rand10(),
        i +=1
