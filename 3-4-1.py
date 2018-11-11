# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:00:44 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

class  Test:

    def  __init__(self):
        self.maxSum= -2**31
    """
    方法功能：求最大子树
    输入参数：root:根结点；
    maxRoot最大子树的根结点
    返回值：以root为根结点子树所有结点的和
    """
    def  findMaxSubTree(self,root,maxRoot):
        if  root==None:
            return  0
        #求root左子树所有结点的和
        lmax = self.findMaxSubTree(root.lchild,maxRoot)
        # 求root右子树所有结点的和
        rmax = self.findMaxSubTree(root.rchild,maxRoot)
        sums=lmax+rmax+root.data
        #以root为根的子树的和大于前面求出的最大值
        if  sums > self.maxSum:
            self.maxSum=sums
            maxRoot.data=root.data
        # 返回以root为根结点的子树的所有结点的和
        return  sums

    """
    方法功能：构造二叉树
    返回值：返回新构造的二叉树的根结点
    """
    def  constructTree(self):
        root=BiTNode()
        node1=BiTNode()
        node2=BiTNode()
        node3=BiTNode()
        node4=BiTNode()
        root.data=6
        node1.data=3
        node2.data=-7
        node3.data=-1
        node4.data=9
        root.lchild=node1
        root.rchild=node2
        node1.lchild=node3
        node1.rchild=node4
        node2.lchild=node2.rchild=node3.lchild=node3.rchild= \
        node4.lchild=node4.rchild=None
        return  root

if  __name__=="__main__": 
    # 构造二叉树
    test=Test()
    root=test.constructTree()

    maxRoot=BiTNode() # 最大子树的根结点
    test.findMaxSubTree(root,maxRoot)
    print  "最大子树和为："+str(test.maxSum)
    print  "对应子树的根结点为："+str(maxRoot.data)
