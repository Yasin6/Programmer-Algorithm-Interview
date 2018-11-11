# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:02:15 2018

@author: Administrator
"""

class  Test:
    def  __init__(self):
        self.center=None
        self.palindromeLen=None        
    def  getCenter(self):return  self.center
    def  getLen(self): return  self.palindromeLen    
    def  mins(self,a,b):
        return  b if  a>b else a
    """
    方法功能：找出字符串最长的回文子串
    输入参数：str为字符串，center为回文字符的中心字符，len表示回文字符串长度
    如果长度为偶数，那么表示中间偏左边的那个字符的位置
    """
    def  Manacher(self,strs):
        lens=len(strs)  # 字符串长度
        newLen=2*lens+1 
        s=[None]*newLen # 插入分隔符后的字符串
        p=[None]*newLen
        id=0	     # id表示以第id个字符为中心的回文字符串最右端的下标值最大
        i=0
        while  i < newLen:
            # 构造填充字符串	
            s[i] = '*'
            p[i] = 0
            i +=1
        i=0
        while  i<lens:
            s[(i + 1) *2] = list(strs)
            i +=1
        self.center=-1
        self.palindromeLen = -1
        # 求解p数组
        i=1
        while  i<newLen:
            if  id+p[id] > i: # 图中（1），（2），(3)三种情况
                p[i] = self.mins(id+p[id]-i, p[2*id - i])
            else:    # 对应图中第（4）种情况
                p[i] = 1
            # 然后接着向左右两边扩展求最长的回文子串
            while  i + p[i]<newLen and i - p[i]>0 and s[i - p[i]] == s[i + p[i]]:
                p[i] +=1
            # 当前求出的回文字符串最右端的下标更大
            if  i + p[i] > id+p[id]:
                id = i
            # 当前求出的回文字符串更长
            if  p[i] - 1 > self.palindromeLen:
                self.center=(i+1)/2-1
                self.palindromeLen = p[i] - 1	# 更新最长回文子串的长度
            i +=1
			
if  __name__=="__main__":
    strs="abcbax"
    t=Test()
    t.Manacher(strs)
    center=t.getCenter()
    palindromeLen=t.getLen()
    if  center!=-1 and palindromeLen!=-1:
        print  "最长的回文子串为：",
        # 回文字符串长度为奇数
        if  palindromeLen % 2 ==1:
            i=center-palindromeLen/2
            while  i<=center+palindromeLen/2:
                print  list(strs)[i],
                i +=1
        # 回文字符串长度为偶数
        else:
            i=center-palindromeLen/2
            while  i<center+palindromeLen/2:
                print  list(strs)[i],
                i +=1
    else:
        print  "查找失败"
