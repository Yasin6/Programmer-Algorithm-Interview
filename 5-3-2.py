# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:37:28 2018

@author: Administrator
"""

def  reverseStr(strs):
    ch=list(strs)
    lens=len(ch)
    i=0
    j=lens-1
    while  i<j:
        #Python中不能直接对字符串进行异或操作，所以借助ord和chr函数。
        ch[i]=chr(ord(ch[i])^ord(ch[j]))  
        ch[j]=chr(ord(ch[i])^ord(ch[j]))
        ch[i]=chr(ord(ch[i])^ord(ch[j]))
        i +=1
        j -=1
    return  ''.join(ch)
