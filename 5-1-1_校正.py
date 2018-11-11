# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:30:02 2018

@author: Administrator
"""

# 交换字符数组下标为i和j对应的字符 
def  swap(str,i,j):
    tmp=str[i]
    str[i]=str[j]
    str[j]=tmp

"""
方法功能：对字符串中的字符进行全排列
输入参数：str为待排序的字符串，start为待排序的子字符串的首字符下标
"""
def  Permutation(str,start):
    if  str==None or start<0: #书中两个等号之间有空白
        return  
    # 完成全排列后输出当前排列的字符串
    if  start==len(str)-1  :
        print  ''.join(str),
    else: 
        i=start
        while  i<len(str):
            # 交换start与i所在位置的字符
            swap(str,start,i)
            # 固定第一个字符，对剩余的字符进行全排列
            Permutation(str, start+1)
            # 还原start与i所在位置的字符
            swap(str,start,i)
            i +=1

def  Permutation_transe(s):
    str=list(s)
    Permutation(str,0)

if  __name__=="__main__":  #书中两个等号之间有空白
    s = "abc"
    Permutation_transe(s)
