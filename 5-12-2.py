# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:03:58 2018

@author: Administrator
"""

def  isDup(strs):
    lens=len(strs)
    flags=[None]*8  # 只需要8个32位的int，8*32=256位
    i=0
    while  i<8:
        flags[i]=0
        i +=1
    i=0
    while  i<lens:
        index=ord(list(strs)[i])/32
        shift=ord(list(strs)[i])%32
        if  (flags[index] & (1<<shift))!=0:
            return  True
        flags[index] |=(1<<shift)
    return  False

if  __name__=="__main__":
    strs="GOOD"
    result=isDup(strs)
    if  result:
        print  strs+"中有重复字符"
    else:
        print  strs+"中没有重复字符"

