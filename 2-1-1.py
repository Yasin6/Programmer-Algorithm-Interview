# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:34:38 2018

@author: Administrator
"""

class  MyStack:
    # 模拟栈
    def  __init__(self): 
        self.items= []        
    # 判断栈是否为空
    def  isEmpty(self): 
        return  len(self.items) ==0  
    # 返回栈的大小
    def  size(self): 
        return  len(self.items) 
    # 返回栈顶元素
    def  top(self): 
        if  not self.isEmpty(): 
            return  self.items[len(self.items)-1] 
        else:
            return  None
    # 弹栈
    def  pop(self):
        if  len(self.items)>0:
            return  self.items.pop()  
        else:
            print  "栈已经为空"
            return  None
    # 压栈
    def  push(self,item): 
        self.items.append(item) 

if  __name__=="__main__":   
    s=MyStack() 
    s.push(4)   
    print   "栈顶元素为：" +str(s.top())
    print   "栈大小为：" +str(s.size())
    s.pop()
    print   "弹栈成功"
    s.pop()

