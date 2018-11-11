# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:38:10 2018

@author: Administrator
"""

def  select_sort(lists):
    # 选择排序
    count = len(lists)
    for  i  in  range(0, count):
        min = i
        for  j  in  range(i + 1, count):
            if  lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return  lists

if  __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print  '排序前序列为:',
    for  i  in  (lists):
        print  i,
    print  '\n排序后结果为:', 
    for  i  in  (select_sort(lists)):
        print  i,
