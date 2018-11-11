# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:59:42 2018

@author: Administrator
"""

def  printAtLevel(root,level):

    if  root==None or level < 0:
        return  0
    elif  level == 0:
        print  root.data
        return  1
    else:
        # 把打印根结点level层的结点转换为求解根结点的孩子结点的level-1层的结点。
    return  printAtLevel(root.lchild, level - 1)+
           printAtLevel(root.rchild, level - 1)

