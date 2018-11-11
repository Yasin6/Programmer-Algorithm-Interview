# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:05:34 2018

@author: Administrator
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

"""
方法功能：打印出满足所有结点数据的和等于num的所有路径
参数：root:二叉树根结点；num:给定的整数；sum: 当前路径上所有结点的和
用来存储从根结点到当前遍历到结点的路径
"""
def  FindRoad(root,num,sums,v):
    # 记录当前遍历的root结点
    sums +=root.data  
    v.append(root.data)  
    # 当前结点是叶子结点且遍历的路径上所有结点的和等于num
    if  root.lchild==None and root.rchild== None and  sums==num:
        i=0
        while  i<len(v):
            print  v[i],
            i +=1
        print  '\n'   
    # 遍历root的左子树
    if  root.lchild!=None:
        FindRoad(root.lchild,num,sums,v) 
    # 遍历root的右子树
    if  root.rchild!=None:
        FindRoad(root.rchild,num,sums,v)  
    # 清除遍历的路径
    sums -= v[-1]
    v.remove(v[-1])

def  constructTree():
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
    node2.lchild=node2.rchild=node3.lchild=node3.rchild=node4.lchild=node4.rchild=None
    return  root

if  __name__=="__main__": 
    root=constructTree()
    s=[]
    print  "满足路径结点和等于8的路径为：",
    FindRoad(root,8,0,s)
