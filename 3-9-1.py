# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:05:06 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

def  createDupTree(root):
    if  root==None:
        return  None
    # 二叉树根结点
    dupTree=BiTNode()
    dupTree.data=root.data
    # 复制左子树
    dupTree.lchild=createDupTree(root.lchild)
    # 复制右子树
    dupTree.rchild=createDupTree(root.rchild)
    return  dupTree

def  printTreeMidOrder(root): 
    if  root==None:
        return
    # 遍历root结点的左子树
    if  root.lchild!=None:
        printTreeMidOrder(root.lchild)
    # 遍历root结点
    print  root.data,
    # 遍历root结点的右子树
    if  root.rchild!=None:
        printTreeMidOrder(root.rchild)

if  __name__=="__main__":
    root1=constructTree()  #引用3.4节
    root2=createDupTree(root1)
    print  "原始二叉树中序遍历：",
    printTreeMidOrder (root1) 
    print  '\n'
    print  "新的二叉树中序遍历：",
    printTreeMidOrder(root2)
