# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:39:09 2018

@author: Administrator
"""

def  merge(left, right):
    i, j = 0, 0
    result = []
    while  i < len(left) and j < len(right):
        if  left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return  result

def  merge_sort(lists):
    # 归并排序
    if  len(lists) <= 1:
        return  lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return  merge(left, right)

if  __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print  '排序前序列为:',
    for  i  in  lists:
        print  i,
    print  '\n排序后结果为:', 
    for  i  in  (merge_sort(lists)):
        print  i,

