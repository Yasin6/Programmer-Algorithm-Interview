# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:36:45 2018

@author: Administrator
"""

def  reverseStr(str):
    ch=list(str)
    lens=len(ch)
    i=0
    j=lens-1
    while  i<j:
        tmp=ch[i]
        ch[i]=ch[j]
        ch[j]=tmp
        i +=1
        j -=1
    return  ''.join(ch)
	
if  __name__=="__main__":  #书中2个等号之间有空格
    str="abcdefg"
    print  "字符串"+str+"翻转后为：",
    print  reverseStr(str)
