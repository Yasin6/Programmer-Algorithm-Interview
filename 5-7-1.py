# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:44:31 2018

@author: Administrator
"""

# 方法功能：去掉字符串中嵌套的括号 
def  removeNestedPare(strs):
    if   strs==None:
        return  strs
    Parentheses_num = 0 # 用来记录不匹配的“（”出现的次数
    if  list(strs)[0] !='(' or list(strs)[-1] !=')':
        return  None
    sb='('
    # 字符串首尾的括号可以单独处理
    i=1
    while  i<len(strs)-1:
        ch = list(strs)[i]
        if  ch == '(':
            Parentheses_num +=1
        elif  ch == ')':
            Parentheses_num -=1
        else:
            sb=sb+(list(strs)[i])
        i +=1
    # 判断括号是否匹配
    if  Parentheses_num !=0:
        print  "由于括号不匹配，因此不做任何操作"
        return  None
    # 处理字符串结尾的")"
    sb=sb+')'
    return  sb

if  __name__=="__main__":
    strs="(1,(2,3),(4,(5,6),7))"
    print  strs+"去除嵌套括号后为："+removeNestedPare(strs)
