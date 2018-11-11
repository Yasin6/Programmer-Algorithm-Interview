# -*- coding: utf-8 -*-
"""
Created on Wed Nov 07 22:49:29 2018

@author: Administrator
"""

def bubble_sort(lists):
    for i in range(len(lists)-1):    
        for j in range(len(lists)-i-1):  
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists


if __name__=="__main__":  
    lists=[3,4,2,8,9,5,1]
    print '排序前序列为:',
    for i in (lists):
        print i,
    print '\n排序后结果为:', 
    for i in (bubble_sort(lists)):
        print i,