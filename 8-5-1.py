# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:39:30 2018

@author: Administrator
"""

def  quick_sort(lists, left, right):
    # 快速排序
    if  left >= right:
        return  lists
    key = lists[left]
    low = left
    high = right
    while  left < right:
        while  left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while  left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return  lists

if  __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print  '排序前序列为:',
    for  i  in  (lists):
        print  i,
    print  '\n排序后结果为:', 
    for  i  in  (quick_sort(lists,0,len(lists)-1)):
        print  i,
