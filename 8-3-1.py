# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:38:49 2018

@author: Administrator
"""

def  bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for  i  in  range(0, count):
        for  j  in  range(i + 1, count):
            if  lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return  lists

if  __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print  '排序前序列为:',
    for  i  in  lists:
        print  i,
    print  '\n排序后结果为:', 
    for  i  in  (bubble_sort(lists)):
        print  i,
