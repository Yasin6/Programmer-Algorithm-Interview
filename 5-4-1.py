# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:41:09 2018

@author: Administrator
"""

"""
方法功能：判断两个字符串是否为换位字符串
输入参数：s1与s2为两个字符串
返回值：如果是返回true，否则返回false
"""
def  compare(s1,s2):
    result=True
    bCount=[None]*256
    i=0
    while  i<256:
        bCount[i]=0
        i +=1
    i=0
    while  i<len(s1):
        bCount[ord(list(s1)[i])-ord('0')] +=1
        i +=1
    i=0
    while  i<len(s2):
        bCount[ord(list(s2)[i])-ord('0')] -=1
        i +=1
    i=0
    while  i<256:
        if  bCount[i] !=0:
            result=False
            break;
        i +=1
    return  result;

if  __name__=="__main__":  #校正
    str1="aaaabbc";
    str2="abcbaaa";
    print  str1+"和"+str2,
    if  compare(str1,str2):
        print  "是换位字符"
    else:
        print  "不是换位字符"


