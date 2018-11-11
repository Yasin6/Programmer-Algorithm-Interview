# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:40:12 2018

@author: Administrator
"""

def  adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    maxs = i
    if  i < size / 2:
        if  lchild < size and lists[lchild] > lists[maxs]:
            maxs = lchild
        if  rchild < size and lists[rchild] > lists[maxs]:
            maxs = rchild
        if  maxs != i:
            lists[maxs], lists[i] = lists[i], lists[maxs]
            adjust_heap(lists, maxs, size)

def  build_heap(lists, size):
    for  i  in  range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def  heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for  i  in  range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)

if  __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print  '排序前序列为:',
    for  i  in  lists:
        print  i,
    print  '\n排序后结果为:', 
    heap_sort(lists)
    for  i  in  lists:
        print  i,

