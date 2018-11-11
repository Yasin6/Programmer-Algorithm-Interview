# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:38:08 2018

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

def  isPopSerial(push,pop):  
    if  push==None or pop==None:
        return  False
    pushLen=len(push)
    popLen=len(pop)
    if  pushLen!=popLen:
        return  False
    pushIndex=0
    popIndex=0
    stack =Stack()
    while  pushIndex < pushLen:
        # 把push序列依次入栈，直到栈顶元素等于pop序列的第一个元素
        stack.push(push[pushIndex])
        pushIndex +=1
            # 栈顶元素出栈，pop序列移动到下一个元素
        while  (not stack.empty() ) and stack.peek()== pop[popIndex]:
            stack.pop()
            popIndex +=1	
    #栈为空，且pop序列中元素都被遍历过
    return  stack.empty() and popIndex==popLen

if  __name__=="__main__":
    push="12345"
    pop="32541"
    if  isPopSerial(push,pop):
        print  pop+"是"+push+"的一个pop序列"
    else:
        print  pop+"不是"+push+"的一个pop序列"
