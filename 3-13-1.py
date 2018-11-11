# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:06:45 2018

@author: Administrator
"""

class  TreeNode:
    def  __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class  IntRef:
    def  __init__(self):
        self.val=None

# 求a，b，c的最大值
def  Max(a,b,c):
    maxs = a if  a>b else b
    maxs = maxs if  maxs>c else c
    return  maxs

# 寻找最长路径
def  findMaxPathRecursive(root,maxs):
    if  None == root:
        return  0
    else:
        # 求左子树以root.left为起始结点的最大路径和
        sumLeft = findMaxPathRecursive(root.left,maxs)
        # 求右子树以root.right为起始结点的最大路径和
        sumRight = findMaxPathRecursive(root.right,maxs)        
        # 求以root为起始结点，叶子结点为结束结点的最大路径和
        allMax = root.val + sumLeft + sumRight
        leftMax = root.val + sumLeft
        rightMax = root.val + sumRight
        tmpMax = Max(allMax, leftMax, rightMax)
        if  tmpMax>maxs.val:
				maxs.val = tmpMax
        subMax = sumLeft if  sumLeft > sumRight else sumRight
        # 返回以root为起始结点，叶子结点为结束结点的最大路径和
        return  root.val + subMax
	
def  findMaxPath(root):
    maxs=IntRef()
    maxs.val = -2**31
    findMaxPathRecursive(root,maxs)
    return  maxs.val

if  __name__=="__main__": 
    root =TreeNode(2)
    left =TreeNode(3)
    right =TreeNode(5)
    root.left = left
    root.right = right
    print  findMaxPath(root)
