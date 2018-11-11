# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:07:57 2018

@author: Administrator
"""

"""
方法功能：在数组中找唯一重复的元素
输入参数：array:数组对象的引用
 返回值：重复元素的值，如果无重复元素则返回-1
"""
#使用字典
def  findDup(array):
    if  None==array:
		return  -1
    lens=len(array)
    hashTable=dict()
    i=0
    while  i <lens - 1 :
        hashTable[i]=0
        i +=1
    j=0
    while  j<lens:
        if  hashTable[array[j]-1] == 0:
             hashTable[array[j] - 1]=array[j] - 1
        else:
            return  array[i]
        j +=1
    return  -1

if  __name__=="__main__":
    array= [1, 3, 4, 2, 5, 3 ]
    print  findDup(array)
