# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:06:26 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None
"""       
方法功能：查找值最小的结点
输入参数：root:根结点
返回值：值最小的结点
"""
def  getMinNode(root):
    if  root==None:
        return  root
    while  root.lchild!=None:
        root=root.lchild
    return  root
"""	
方法功能：查找值最大的结点
输入参数：root:根结点
返回值：值最大的结点
"""
def  getMaxNode(root):
    if  root==None:
        return  root
    while  root.rchild!=None:
        root=root.rchild
    return  root

def  getNode(root):
    maxNode=getMaxNode(root)
    minNode=getMinNode(root)
    mid=(maxNode.data+minNode.data)/2
    result=None    
    while  root!=None:
        # 当前结点的值不大于f，则在右子树上找
        if  root.data<=mid:
            root=root.rchild  
        #否则在左子树上找
        else:
            result=root  
            root=root.lchild  
    return  result  

if  __name__=="__main__": 
    arr=[1,2,3,4,5,6,7]
    root=arraytotree(arr,0,len(arr)-1)  # 3.2节
    print  getNode(root).data
