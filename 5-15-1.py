# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:05:38 2018

@author: Administrator
"""

# 函数功能：求字符串L的最长递增子串的长度 
def  getMaxAscendingLen(strs):
    lens = len(strs)
    maxLen =[None] * lens
    maxLen[0] = 1
    maxAscendingLen = 1
    i=1
    while  i<lens:
        maxLen[i]=1 # maxLen[i]的最小值为1；
        j=0
        while  j<i:
            if  list(strs)[j] < list(strs)[i] and maxLen[j] > maxLen[i]-1:
                maxLen[i]=maxLen[j]+1
                maxAscendingLen=maxLen[i]
            j +=1
        i +=1
    return  maxAscendingLen

if  __name__=="__main__":
    s = "xbcdza"
print  "最长递增子序列的长度为："+ str(getMaxAscendingLen(s))
