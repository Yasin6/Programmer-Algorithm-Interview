# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:00:59 2018

@author: Administrator
"""

class  Test:
    def  __new__(self):
        self.startIndex=None
        self.lens=None       
    def  getStartIndex(self): return  self.startIndex
    def  getLen(self): return  self.lens
    """
    方法功能：找出字符串中最长的回文子串
    输入参数：str为字符串，startIndex与len为找到的回文字符串的起始位置与长度
    """
    def  getLongestPalindrome(self,strs):
        if  strs==None:
            return  
        n = len(strs) # 字符串长度
        if  n<1:
            return
        self.startIndex = 0
        self.lens = 1
        # 申请额外的存储空间记录查找的历史信息
        historyRecord=[([None]*n)  for  i  in  range (n)]
        i=0
        while  i<n:
            j=0
            while  j<n:
                historyRecord[i][j]=0
                j +=1
            i +=1
        # 初始化长度为1的回文字符串信息
        i=0
        while  i<n:
            historyRecord[i][i] = 1 
            i +=1
        # 初始化长度为2的回文字符串信息
        i =0
        while  i<n-1:
            if  list(strs)[i] == list(strs)[i+1]:
                historyRecord[i][i+1] = 1
                self.startIndex = i
                self.lens = 2
            i +=1           
        # 查找从长度为3开始的回文字符串
        pLen = 3
        while  pLen <= n:
            i=0
            while  i < n-pLen+1:
                j = i+pLen-1
                if  list(strs)[i] == list(strs)[j] and historyRecord[i+1][j-1] ==1:
                    historyRecord[i][j] = 1
                    self.startIndex = i
                    self.lens = pLen
                i +=1
            pLen +=1

if  __name__=="__main__":
    strs="abcdefgfedxyz"   
    t=Test()
    t.getLongestPalindrome(strs)
    if  t.getStartIndex()!=-1 and t.getLen()!=-1:
        print  "最长的回文字串为：",
        i=t.getStartIndex()
        while  i<t.getStartIndex()+t.getLen():
            print  list(strs)[i],
            i +=1
    else:
        print  "查找失败"
