# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:37:26 2018

@author: Administrator
"""

#  引申：如何给栈排序
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

"""
方法功能：把栈底元素移动到栈顶
参数：s 栈的引用

"""
def  moveBottomToTop(s):
    if  s.empty():
        return
    top1=s.peek()
    s.pop()
    if  not s.empty():
        moveBottomToTop(s)
        top2=s.peek()
        if  top1>top2:
            s.pop()
            s.push(top1)
            s.push(top2)
            return
    s.push(top1)
	
def  sortStack(s):
    if  s.empty():
        return
    # 把栈底元素移动到栈顶
    moveBottomToTop(s)
    top=s.peek()
    s.pop()
    # 递归处理子栈
    sortStack(s)
    s.push(top)

if  __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(3)
    s.push(2)
    sortStack(s)
    print  "排序后出栈顺序为:",
    while  not s.empty():
        print  s.peek(),
        s.pop()
