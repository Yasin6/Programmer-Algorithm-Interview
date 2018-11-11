# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:03:30 2018

@author: Administrator
"""

# 判断字符串中是否有相同的字符 
def  isDup(strs):
    lens=len(strs)
    i=0
    while  i<lens:
        j=i+1
        while  j<lens:
            if  list(strs)[j] ==list(strs)[i]:
                return  True
            j +=1
        i +=1
    return  False

if  __name__=="__main__":
    strs="GOOD"
    result=isDup(strs)
    if  result:
        print  strs+"中有重复字符"
    else:
        print  strs+"中没有重复字符"
