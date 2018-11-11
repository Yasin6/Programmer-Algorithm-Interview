# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:02:59 2018

@author: Administrator
"""

"""
方法功能：判断一个数组是否是二元查找树的后续遍历序列
输入参数：arr:数组；
返回值：true:是，否则返回false
"""
def  IsAfterOrder(arr,start,end):
    if  arr==None:
        return  False
    # 数组的最后一个结点必定是根结点
    root=arr[end]
    # 找到第一个大于root的值，那么前面所有的结点都位于root的左子树上
    i=start
    while  i<end:
        if(arr[i]>root):
            break
        i +=1
    # 如果序列是后续遍历的序列，那么从i开始的所有值都应该大于根结点root的值
    j=i
    while  j<end:
        if  arr[j]<root:
            return  False
        j +=1   
    left_IsAfterOrder = True
    right_IsAfterOrder = True 
    # 判断小于root值的序列是否是某一二元查找树的后续遍历
    if  i > start: 
        left_IsAfterOrder = IsAfterOrder(arr,start, i-1)  
    # 判断大于root值的序列是否是某一二元查找树的后续遍历
    if  j < end: 
        right_IsAfterOrder = IsAfterOrder(arr,i, end)    
    return  left_IsAfterOrder and right_IsAfterOrder 

if  __name__=="__main__":
    arr=[1,3,2,5,7,6,4]
    result=IsAfterOrder(arr,0,len(arr)-1)
    i=0
    while  i<len(arr):
        print  arr[i],
        i +=1
    if  result:
        print  "是某一二元查找树的后续遍历序列"
    else:
        print  "不是某一二元查找树的后续遍历序列"
