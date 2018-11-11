# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:39:01 2018

@author: Administrator
"""

class  Stack:
    # 模拟栈
    def  __init__(self): 
        self.items= []        
    # 判断栈是否为空
    def  empty(self): 
        return  len(self.items) ==0  
    # 返回栈的大小
    def  size(self): 
        return  len(self.items) 
    # 返回栈顶元素
    def  peek(self): 
        if  not self.empty(): 
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


class  MyStack:
    def  __init__(self): 
        self.A=Stack() # 用来存储栈中元素 

        self.B=Stack() # 用来存储当前栈中最小的元素      
    def  push(self,data):
        self.A.push(data)      
    def  pop(self):
        if  self.B.empty():
            while  not self.A.empty():
                self.B.push(self.A.peek())
                self.A.pop()
        first=self.B.peek()
        self.B.pop()
        return  first
	
if  __name__=="__main__":
    stack= MyStack()
    stack.push(1)
    stack.push(2)
    print  "队列首元素为："+str(stack.pop())
    print  "队列首元素为："+str(stack.pop())

