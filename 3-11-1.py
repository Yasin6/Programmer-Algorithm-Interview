# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:06:01 2018

@author: Administrator
"""

from  collections  import  deque

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

# 对二叉树进行镜像反转 
def  reverseTree(root):
    if  root==None:
        return
    reverseTree(root.lchild)
    reverseTree(root.rchild)
    tmp=root.lchild
    root.lchild=root.rchild
    root.rchild=tmp

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
        root =None
    return  root

def  printTreeLayer(root):
    if  root==None:
        return
    queue=deque()
    # 树根结点进队列
    queue.append(root)
    while  len(queue)>0:
        p=queue.popleft()
        # 访问当前结点
        print  p.data,
        # 如果这个结点的左孩子不为空则入队列
        if  p.lchild!=None:
            queue.append(p.lchild)
        # 如果这个结点的右孩子不为空则入队列
        if  p.rchild!=None:
         queue.append(p.rchild)

if  __name__=="__main__": 
    arr=[1,2,3,4,5,6,7]
    root=arraytotree(arr, 0,len(arr)-1)
    print  "二叉树层序遍历结果为：",
    printTreeLayer(root)
    print  '\n'
    reverseTree(root)
    print  "反转后的二叉树层序遍历结果为：",
    printTreeLayer(root)  

