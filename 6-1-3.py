# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:17:54 2018

@author: Administrator
"""

def  isPower(n):
    minus=1;
    while  n>0:
        n=n-minus;
        # n是某个数的平方
        if  n==0:
            return  True;
        # n不是某个数的平方
        elif  n<0:
            return  False;
        # 每次减数都加2
        else:
            minus +=2;
    return  False

if  __name__=="__main__":
    n1=15
    n2=16
    if  isPower(n1):
        print  str(n1)+"是某个自然数的平方"
    else:
        print  str(n1)+"不是某个自然数的平方"
    if  isPower(n2):
        print  str(n2)+"是某个自然数的平方"
    else:
        print  str(n2)+"不是某个自然数的平方"
