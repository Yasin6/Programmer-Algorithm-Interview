# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:04:37 2018

@author: Administrator
"""

def  FindParentNode(root,node1,node2):
    if  None == root or root == node1 or root == node2:
        return  root
    lchild = FindParentNode(root.lchild, node1, node2)
    rchild = FindParentNode(root.rchild, node1, node2)
    # root的左子树中没有结点node1和node2,那么一定在root的右子树上
    if  None == lchild:
        return  rchild
    # root的右子树中没有结点node1和node2,那么一定在root的左子树上
    elif  None== rchild:
        return  lchild
    # node1与node2分别位于root的左子树与右子树上，root就是它们最近的共同父结点
    else:
        return  root
