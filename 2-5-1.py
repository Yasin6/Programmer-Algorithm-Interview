# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:38:34 2018

@author: Administrator
"""

# 模拟栈
class  Stack:
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


class  MyStack :
    def  __init__(self): 
        self.elemStack=Stack() # 用来存储栈中元素 
        self.minStack=Stack() # 栈顶永远存储当前elemStack中最小的值     
    def  push(self,data):
        self.elemStack.push(data)
        # 更新保存最小元素的栈
        if  self.minStack.empty():
            self.minStack.push(data)
        else:
            if  data < self.minStack.peek():
                self.minStack.push(data)   
    def  pop(self):
        topData = self.elemStack.peek()
        self.elemStack.pop()
        if  topData == self.mins():
            self.minStack.pop()
        return  topData  
    def  mins(self):
        if  self.minStack.empty():
            return  2 ** 32
        else:
            return  self.minStack.peek()

if  __name__=="__main__":
    stack = MyStack()
    stack.push(5)
    print  "栈中最小值为：" + str(stack.mins())
    stack.push(6)
    print  "栈中最小值为：" + str(stack.mins())
    stack.push(2)
    print  "栈中最小值为：" + str(stack.mins())
    stack.pop()
    print  "栈中最小值为：" + str(stack.mins())
