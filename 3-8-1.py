# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:03:31 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

class  stack:
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
    def  peek(self): 
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

"""
方法功能：获取二叉树从根结点root到node结点的路径
输入参数：root:根结点；node:二叉树中的某个结点；s：用来存储路径的栈
返回值：node在root的子树上，或node==root时返回true，否则返回false
"""
def  getPathFromRoot(root,node,s):
    if  root == None:
        return  False
    if  root == node:
        s.push(root)
        return  True
    """
    如果node结点在root结点的左子树或右子树上，
    那么root就是node的祖先结点，把它加到栈里
    """
    if  getPathFromRoot(root.lchild, node,s) or getPathFromRoot(root.rchild, node,s):
        s.push(root)
        return  True
    return  False

"""
方法功能：查找二叉树中两个结点最近的共同父结点
输入参数：root:根结点；node1与node2为二叉树中两个结点
返回值：node1与node2最近的共同父结点
"""
def  FindParentNode(root,node1,node2):   
    stack1=stack()  # 保存从root到node1的路径
    stack2=stack() # 保存从root到node2的路径
    # 获取从root到node1的路径
    getPathFromRoot(root, node1,stack1)  
    # 获取从root到node2的路径
    getPathFromRoot(root, node2, stack2)
    commonParent = None
    # 获取最靠近node1和node2的父结点
    while  stack1.peek()== stack2.peek():
        commonParent = stack1.peek()
        stack1.pop()
        stack2.pop()
    return  commonParent

if  __name__=="__main__":
    arr= [1,2,3,4,5,6,7,8,9,10]
    root=arraytotree(arr,0,len(arr)-1) 
    node1=root.lchild.lchild.lchild
    node2=root.lchild.rchild
    res=None
    res = FindParentNode(root,node1,node2)		
    if  res != None:
        print  str(node1.data)+"与"+str(node2.data)+"的最近公共父结点为："+str(res.data),
    else:
        print  "没有公共父结点"
