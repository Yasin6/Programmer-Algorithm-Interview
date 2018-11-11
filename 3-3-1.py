# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:58:58 2018

@author: Administrator
"""

from  collections  import  deque

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

# 方法功能：把有序数组转换为二叉树	
def  arraytotree(arr,start,end):
    root=None
    if  end>=start:
        root =BiTNode();
        mid=(start+end+1)/2;
        # 树的根结点为数组中间的元素
        root.data = arr[mid];
        # 递归的用左半部分数组构造root的左子树
        root.lchild=arraytotree(arr,start,mid-1);
        # 递归的用右半部分数组构造root的右子树
        root.rchild=arraytotree(arr, mid+1, end);      

    else:
        root = None
    return  root

"""
方法功能：用层序遍历的方式打印出二叉树结点的内容
输入参数：root:二叉树根结点
"""
def  printTreeLayer(root):
    if  root==None:
        return;
    queue=deque()
    # 树根结点进队列
    queue.append(root)    
    while  len(queue)>0:
        p=queue.popleft()
        # 访问当前结点
        print(p.data),
        # 如果这个结点的左孩子不为空则入队列
        if  p.lchild !=None:
            queue.append(p.lchild)
        # 如果这个结点的右孩子不为空则入队列
        if  p.rchild!=None:
            queue.append(p.rchild);	

if  __name__=="__main__": 
    arr=[1,2,3,4,5,6,7,8,9,10]
    root=arraytotree(arr, 0,len(arr)-1); 
    print  "树的层序遍历结果为:",
    printTreeLayer (root);
