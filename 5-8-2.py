# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:47:33 2018

@author: Administrator
"""

class  Test:
    def  __init__(self):
        self.flag=None       
    def  getFlag(self): return  self.flag
    # 判断c是否是数字，如果是返回True，否则返回False 
    def  isNumber(self,c):
        return  c>='0'and c<='9'
    def  strToint(self,strs):
        if  strs==None:
            self.flag=False
            print  "不是数字"
            return  -1
        self.flag=True
        res = 0
        i = 0
        minus = False # 是否是负数
        if  list(strs)[i] == '-': # 结果是负数
            minus = True 
            i +=1
        if  list(strs)[i] == '+': # 正数
            i +=1
        while  i<len(strs):
            if  self.isNumber(list(strs)[i]):
                res = res * 10 + ord(list(strs)[i]) - ord('0')
            else:
                self.flag=False
                print   "不是数字"
                return  -1
            i +=1
        return  -res if  minus else res

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
    if  t.getFlag():
        print  result
