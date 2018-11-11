# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:39:50 2018

@author: Administrator
"""

def  shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
    while  group > 0:
        for  i  in  range(0, group):
            j = i + group
            while  j < count:
                k = j - group
                key = lists[j]
                while  k >= 0:
                    if  lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return  lists

if  __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print  '排序前序列为:',
    for  i  in  (lists):
        print  i,
    print  '\n排序后结果为:', 
    for  i  in  (shell_sort(lists)):
        print  i,
