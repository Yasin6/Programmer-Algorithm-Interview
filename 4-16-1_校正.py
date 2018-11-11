# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:21:36 2018

@author: Administrator
"""

def  findWithBinary(array,data):
    if  array==None:
        return  False  #书中是首字母小写 false
    # 从二维数组右上角元素开始遍历
    i = 0
    rows=len(array)
    columns = len(array[0])
    j = columns - 1
    while  i< rows and j >= 0:
        # 在数组中找到data，返回
        if  array[i][j] == data:
            return  True  #书中是首字母小写 true
        # 当前遍历到数组中的值大于data，data肯定不在这一列中
        elif  array[i][j] > data:
            j -=1
        # 当前遍历到数组中的值小于data，data肯定不在这一行中
        else:
            i +=1
    return  False

if  __name__=="__main__":
    array=[[0, 1, 2, 3, 4 ],
           [10, 11, 12, 13, 14],
           [20, 21, 22, 23, 24],
           [30, 31, 32, 33, 34],
           [40, 41, 42, 43, 44]]
    print  findWithBinary(array, 17)
    print  findWithBinary(array, 14)
