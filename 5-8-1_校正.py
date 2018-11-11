# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:45:13 2018

@author: Administrator
"""

class  Test:
    def  __init__(self):
        self.flag=None       
    def  getFlag(self): return  self.flag
    # 判断c是否是数字，如果是返回True，否则返回False 
    def  isNumber(self,c):
        return  c>='0'and c<='9'
    """
    判断str是否是数字，如果是返回数字，且设置flag=True,否则设置flag=False
    输入参数：str为字符数组，length为数组长度，flag表示str是否是数字
    """
    def  strtoint(self,strs,length):
        if  length > 1:
            if  not self.isNumber(list(strs)[length - 1]):
                # 不是数字
                print  "不是数字"
                self.flag=False
                return  -1
            if  list(strs)[0] == '-':
                return  self.strtoint(strs,length-1) * 10 - (ord(list(strs)[length - 1]) - ord('0')) 
            else :
                return  self.strtoint(strs,length-1) * 10 + ord(list(strs)[length - 1]) - ord('0')
        else:
            if  list(strs)[0] =='-':
                return  0
            else:
                if  not self.isNumber(list(strs)[0]):
                    print  "不是数字"
                    self.flag=False
                    return  -1
                return  ord(list(strs)[0]) - ord('0')	
    def  strToint(self,s):
        self.flag=True
        if  s==None or len(s)<=0 or (list(s)[0] =='-' and len(s) ==1):
            print  "不是数字"
            self.flag=False
            return  -1
        if  list(s)[0] =='+':
            return  self.strtoint(s[1:len(s)],len(s)-1)
        else:
            return  self.strtoint(s,len(s))  #书中位置没有放对

if  __name__=="__main__":
    t=Test()
    s = "-543"
    print  t.strToint(s)
    s = "543"
    print  t.strToint(s)
    s = "+543"
    print  t.strToint(s)
    s = "++43"
    result=t.strToint(s)
    if  t.getFlag() :
        print  result
