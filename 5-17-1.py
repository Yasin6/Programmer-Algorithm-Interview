# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:06:51 2018

@author: Administrator
"""

# 方法功能：求串中字典序最大的子序列 
def  getLargestSub(src):
    if  src ==None:
        return  None
    lens = len(src)
    largestSub =[None]*(lens+1)
    k=0
    i=0
    while  i<lens:
        largestSub[k] = list(src)[i]
        j=i+1
        while  j<lens:
            # 找出第i个字符后面最大的字符放到largestSub[k]中
            if  list(src)[j] > largestSub[k]:
                largestSub[k]= list(src)[j]
                i=j
            j +=1
        k +=1
        i +=1
    return  ''.join(largestSub[0:k])

if  __name__=="__main__":
    s = "acbdxmng"  
    result = getLargestSub(s)   
    if  result == None:
        print  "字符串为空"
    else:
        print  result
