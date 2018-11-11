# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:04:23 2018

@author: Administrator
"""

class  LongestWord:
    #方法功能：判断字符串strs是否在字符串数组中 
    def  find(self,strArray,strs):
        i=0
        while  i<len(strArray):
            if  strs==strArray[i]:
                return  True
            i +=1
        return  False
    """
    方法功能：判断字符串word是否能由数组strArray中的其他单词组成 
    参数：word为待判断的后缀子串，length待判断字符串的长度
    """
    def  isContain(self,strArray,word,length):
        lens = len(word)
        # 递归的结束条件，当字符串长度为0时，说明字符串已经遍历完了
        if  lens == 0:
            return  True
        # 循环取字符串的所有前缀
        i=1
        while  i<=lens:
            # 取到的子串为自己
            if  i == length:
                return  False
            strs = word[0:i]
            if  self.find(strArray, strs):
                # 查找完字符串的前缀后，递归判断后面的子串能否由其他单词组成
                if  self.isContain(strArray, word[i:], length):
                    return  True
            i +=1
        return  False
    # 方法功能：找出能由数组中其他字符串组成的最长字符串 
    def  getLogestStr(self,strArray):
        # 对字符串由大到小排序
        strArray=sorted(strArray,key=len,reverse=True)
        print  strArray
        # 贪心地从最长的字符串开始判断
        i=0
        while  i<len(strArray):
            if  self.isContain(strArray, strArray[i], len(strArray[i])):
                return  strArray[i]
            i +=1
        # 如果没找到，那么返回空串
        return  None

if  __name__=="__main__":
    strArray=["test", "tester", "testertest", "testing", "apple", "seattle", "banana", "batting",
          "ngcat", "batti", "bat", "testingtester", "testbattingcat" ]
    lw =LongestWord()
    logestStr = lw.getLogestStr(strArray)
    if  logestStr != None:
        print  "最长的字符串为：" + logestStr
    else:
        print  "不存在这样的字符串"
