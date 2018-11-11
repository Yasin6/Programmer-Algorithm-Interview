# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:03:08 2018

@author: Administrator
"""

# 用来存储数对
class  pair: 
    def  __init__(self,first,second):
        self.first=None
        self.second=None
        self.first = first
        self.second = second

def  findPairs(arr):
    # 键为数对的和，值为数对
    sumPair =dict()
    n = len(arr)
    # 遍历数组中所有可能的数对

    i=0
    while  i<n:
        j=i+1
        while  j<n:
            # 如果这个数对的和在map中没有，则放入map中
            sums = arr[i] + arr[j]
            if  sums not in sumPair:
                sumPair[sums]=pair(i, j)
            # map中已经存在与sum相同的数对了，找出来并打印出来
            else:
                # 找出已经遍历过的并存储在map中和为sum的数对
                p = sumPair[sums]
                print"(" + str(arr[p.first]) + ", " + str(arr[p.second]) + ")，(" + \
                str(arr[i]) + ", " + str(arr[j]) + ")"
                return  True
            j +=1
        i +=1            
    return  False

if  __name__=="__main__":
    arr=[3, 4, 7, 10, 20, 9, 8]
    findPairs(arr)
