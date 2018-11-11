# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:57:30 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

# 方法功能：把有序数组转换为二叉树	
def  arraytotree(arr,start,end):
    root=None
    if  end>=start:
        root =BiTNode()
        mid=(start+end+1)/2
        # 树的根结点为数组中间的元素

        root.data = arr[mid]
        # 递归的用左半部分数组构造root的左子树
        root.lchild=arraytotree(arr,start,mid-1)
        # 递归的用右半部分数组构造root的右子树
        root.rchild=arraytotree(arr, mid+1, end)       
    else:
        root = None
    return  root

# 用中序遍历的方式打印出二叉树结点的内容 
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
    arr=[1,2,3,4,5,6,7,8,9,10]
    print  "数组：",
    i=0
    while  i<len(arr):
        print  arr[i],
        i +=1
    print  '\n'
    root=arraytotree(arr, 0,len(arr)-1)
    print  "转换成树的中序遍历为:",
    printTreeMidOrder(root)
    print  '\n'
