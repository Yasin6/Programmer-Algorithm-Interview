# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:27:24 2018

@author: Administrator
"""

"""
方法功能：用+=实现加法操作（限制条件：至少有一个非负数）
输入参数：a,b都是整数，且有一个非负数
返回值：  a+b
"""
def  add(a,b):
    if  a<0 and b<0:
        print  "无法用+=操作实现"
        return  -1
    if  b>=0:
        i=0
        while  i<b:
            a +=1  
            i +=1
        return  a
    else:
        i=0
        while  i<a:
            b +=1 
            i +=1
        return  b

"""
方法功能：用+=实现加减法操作（限制条件：被减数大于减数）
输入参数：a,b都是整数且a>=b
返回值：  a-b
"""
def  minus(a,b):
    if  a<b:
        print  "无法用+=操作实现"
        return  -1
    result = 0  
    while   b!=a:
        b +=1
        result +=1
    return  result    

"""
方法功能：用+=实现加乘法操作（限制条件：两个数都为整数）
输入参数：a,b都是正整数
返回值：  a*b
"""
def  multi(a,b):
    if  a<=0 or b<=0:
        print  "无法用+=操作实现"
        return  -1
    result = 0
    i=0
    while  i<b:
        result = add(result,a)
        i +=1
    return  result    

"""
方法功能：用+=实现加除法操作（限制条件：两个数都为整数）
输入参数：a,b都是正整数
返回值：  a、b
"""
def  divide(a,b):
    if  a<=0 or b<=0:
        print  "无法用+=操作实现"
        return  -1
    result = 1    
    tmpMulti = 0    
    while  True:
        tmpMulti = multi(b,result)    
        if  tmpMulti<=a:
            result +=1    
        else:
            break    
    return  result-1    

if  __name__=="__main__":
    print  add(2,-4)
    print  minus(2,-4)
    print  multi(2,4)
    print  divide(9,4)
