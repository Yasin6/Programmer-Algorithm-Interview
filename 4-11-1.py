# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:18:46 2018

@author: Administrator
"""

# 判断数字n的二进制数从右往左数第i位是否为1
def  isOne(n,i):
    return   (n&(1<<i)) == 1

def  findSingle(arr):
    size=len(arr)
    i=0
    while  i<32:
        result1 = result0 = count1 = count0 = 0
        j=0
        while  j < size:
            if  isOne(arr[j], i):
                result1 ^= arr[j]  # 第i位为1的值异或操作
                count1 +=1         # 第i位为1的数字个数
            else:
                result0^= arr[j] # 第i位为0的值异或操作
                count0 +=1          # 第i位为0的值的个数
            j +=1
        i +=1
        """
        bit值为1的子数组元素个数为奇数，且出现1次的数字被分配到bit值为
        0的子数组，说明只有一个出现1次的数字被分配到bit值为1的子数组中，
        异或记过就是这个出现一次的数字
        """      
        if  count1 % 2 == 1 and result0 !=0:
            return  result1
        # 只有一个出现一次的数字被分配到bit值为0的子数组中
        if  count0 % 2 ==1 and result1 !=0:
           return  result0       
    return  -1

if  __name__=="__main__":
    arr=[6,3,4,5,9,4,3]
    result=findSingle(arr)
    if  result !=-1:
        print  result
    else:
        print  "没找到"

