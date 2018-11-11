# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:03:59 2018

@author: Administrator
"""

import  math
class   BiTNode:
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

class  IntRef:
    def  __init__(self):
        self.num=None

"""
方法功能：找出结点在二叉树中的编号 
输入参数：root:根结点 node:待查找结点；number：node结点在二叉树中的编号
返回值：true:找到该结点的位置，否则返回false
"""
def  getNo(root,node,number):
    if  root == None:
        return  False
    if  root == node:
        return  True
    tmp = number.num
    number.num = 2 * tmp
    # node结点在root的左子树中，左子树编号为当前结点编号的2倍
    if  getNo(root.lchild, node, number):
        return  True
    # node结点在root的右子树中，右子树编号为当前结点编号的2倍加1
    else:
        number.num = tmp * 2 + 1
        return  getNo(root.rchild, node, number)
		
"""
方法功能：根据结点的编号找出对应的结点 
输入参数：root:根结点；number为结点的编号 
返回值：编号为number对应的结点
"""
def  getNodeFromNum(root,number):
    if  root == None or number < 0:
        return  None
    if  number == 1:
        return  root
    # 结点编号对应二进制的位数（最高位一定为1，因为根结点代表1）
    lens = int((math.log(number) / math.log(2)))
    # 去掉根结点表示的1
    number -= 1 << lens
    while  lens>0:
        # 如果这一位二进制的值为1，
        # 那么编号为number的结点必定在当前结点的右子树上 
        if  (1 << (lens - 1)) & number== 1:
            root = root.rchild
        else:
            root = root.lchild
        lens -=1
    return  root

"""
方法功能：查找二叉树中两个结点最近的共同父结点 
输入参数：root:根结点；node1与node2为二叉树中两个结点
返回值：node1与node2最近的共同父结点
"""
def  FindParentNode(root,node1,node2):
    ref1 = IntRef()
    ref1.num = 1
    ref2 = IntRef()
    ref2.num = 1
    getNo(root, node1, ref1)
    getNo(root, node2, ref2)
    num1 = ref1.num
    num2 = ref2.num
    # 找出编号为num1和num2的共同父结点
    while  num1 != num2:
        if  num1 > num2:
            num1 /= 2
        else:
            num2 /= 2
    # num1就是它们最近的公共父结点的编号，通过结点编号找到对应的结点
    return  getNodeFromNum(root, num1)

if  __name__=="__main__":
    arr= [1,2,3,4,5,6,7,8,9,10]
    root=arraytotree(arr,0,len(arr)-1)
    node1=root.lchild.lchild.lchild
    node2=root.lchild.rchild
    res=None
    res = FindParentNode(root,node1,node2)		
    if  res != None:
        print  str(node1.data)+"与"+str(node2.data)+"的最近公共父结点为："+str(res.data),
    else:
        print  "没有公共父结点"

