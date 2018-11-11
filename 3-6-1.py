# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:01:42 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

class  Test:
    def  __init__(self):
        self.pHead=None   # 双向链表头结点
        self.pEnd=None    # 双向链表尾结点

    # 方法功能：把有序数组转换为二叉树	
    def  arraytotree(self,arr,start,end):
        root=None
        if  end>=start:
            root =BiTNode()
            mid=(start+end+1)/2
            # 树的根结点为数组中间的元素
            root.data = arr[mid]
 # 递归的用左半部分数组构造root的左子树
            root.lchild=self.arraytotree(arr,start,mid-1)
            # 递归的用右半部分数组构造root的右子树
            root.rchild=self.arraytotree(arr, mid+1, end)  
        else:
            root = None 
        return  root
    """
    方法功能：把二叉树转换为双向列表
    输入参数：root:二叉树根结点
    """
    def  inOrderBSTree(self,root):
        if  root==None:
            return        
        # 转换root的左子树
        self.inOrderBSTree(root.lchild)
        root.lchild=self.pEnd  # 使当前结点的左孩子指向双向链表中最后一个结点
        if  None==self.pEnd:    #双向列表为空，当前遍历的结点为双向链表的头结点
            self.pHead=root
        else:    # 使双向链表中最后一个结点的右孩子指向当前结点
            self.pEnd.rchild=root
        self.pEnd=root  # 将当前结点设为双向链表中最后一个结点        
        # 转换root的右子树
        self.inOrderBSTree(root.rchild)

if  __name__=="__main__": 
    arr=[1,2,3,4,5,6,7]
    test=Test()
    root=test.arraytotree(arr,0,len(arr)-1) 
    test.inOrderBSTree(root)
    print  "转换后双向链表正向遍历：",
    #cur=BiTNode()
    cur=test.pHead
    while  cur!=None:
        print  cur.data,
        cur=cur.rchild
    print  '\n'
    print  "转换后双向链表逆向遍历：",
    cur=test.pEnd
    while  cur!=None:
        print  cur.data,
        cur=cur.lchild
