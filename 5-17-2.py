# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:07:39 2018

@author: Administrator
"""

def  getLargestSub(src):
    if  src ==None:
        return  None
    lens = len(src)
    largestSub =[None]*(lens+1)
    # 最后一个字符一定在子串中
    largestSub[0] = list(src)[lens-1]
    i = lens-2
    j = 0
    # 逆序遍历字符串
    while  i>0:
        if  ord(list(src)[i])>= ord(largestSub[j]):
            j +=1
            largestSub[j] = list(src)[i]
        i -=1
    #largestSub[j+1]=''
    largestSub=largestSub[0:j+1]
	# 对子串进行逆序
    i=0
    while  i<j:
        tmp=largestSub[i]
        largestSub[i]=largestSub[j]
        largestSub[j]=tmp
        i +=1
        j -=1
    return  ''.join(largestSub)

if  __name__=="__main__":
    s = "acbdxmng"  
    result = getLargestSub(s)   
    if  result == None:
        print  "字符串为空"
    else:
        print  result
