# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:06:00 2018

@author: Administrator
"""

class  CommonSubString:
    # 找出最长的公共子串的长度 
    def  maxPrefix(self,s1,s2):
        i=0
        while  i<len(s1) and i<len(s2):
            if  list(s1)[i] ==list(s2)[i]:
                i +=1
            else:
                break
            i +=1
        return  i      
    # 获取最长的公共子串 
    def  getMaxCommonStr(self,txt):
        n = len(txt)
        # 用来存储后缀数组 
        suffixes=[None]*n
        longestSubStrLen = 0
        longestSubStr=None
        # 获取到后缀数组 
        i=0
        while  i<n:
            suffixes[i] = txt[i:]
            i +=1
        # 对后缀数组排序 
        suffixes.sort()
        i=1
        while  i<n:
            tmp=self.maxPrefix(suffixes[i],suffixes[i-1])
            if  tmp>longestSubStrLen:
                longestSubStrLen = tmp
                longestSubStr=suffixes[i][0:i+1]
            i +=1
        return  longestSubStr

if  __name__=="__main__":
    txt = "banana"
    c=CommonSubString()
    print  "最常的公共子串为："+c.getMaxCommonStr(txt)
