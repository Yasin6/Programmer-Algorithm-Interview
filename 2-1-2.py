# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:35:22 2018

@author: Administrator
"""

class  LNode:
    def  __new__(self,x): 
        self.data=x
        self.next=None

class  MyStack:
    def  __init__(self): 
        # pHead=LNode()
        self.data=None
        self.next=None
    # 判断stack是否为空,如果为空返回true，否则返回false 
    def  empty(self):
         if  self.next == None:
             return  True  
         else:
             return  False   
    # 获取栈中元素的个数
    def  size(self):
        size=0  
        p = self.next  
        while  p != None:
            p = p.next  
            size +=1 
        return  size         
    # 入栈：把e放到栈顶
    def  push(self,e):
        p =LNode   

        p.data = e  
        p.next = self.next  
        self.next = p          
    # 出栈，同时返回栈顶元素
    def  pop(self):
        tmp = self.next  
        if  tmp != None:
            self.next = tmp.next  
            return  tmp.data  
        print  "栈已经为空"
        return  None
    # 取得栈顶元素
    def  top(self):
        if  self.next != None:
            return  self.next.data  
        print  "栈已经为空"  
        return  None    

if  __name__=="__main__":
    stack = MyStack()
    stack.push(1)  
    print  "栈顶元素为："+str(stack.top())
    print  "栈大小为："+str(stack.size())
    stack.pop()
    print  "弹栈成功"
    stack.pop()
