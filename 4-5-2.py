# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:13:17 2018

@author: Administrator
"""

def  get2Num(arr):
    if  arr==None or len(arr)<1:
        print  "参数不合理"
        return
    result = 0
    position = 0
    # 计算数组中所有数字异或的结果
    i=0
    while  i<len(arr):
        result = result^arr[i]
        i +=1
    tmpResult = result   #临时保存异或结果
    # 找出异或结果中其中一个位值为1的位数(如1100，位值为1位数为2和3)
    i=result
    while  i & 1== 0:
        position +=1
        i = i >> 1        
    i=1
    while  i<len(arr):
        # 异或的结果与所有第position位为1的数异或，结果一定是出现一次的两个数中其中一个
        if  ((arr[i] >> position) & 1) ==1:
            result = result^arr[i]
        i +=1
    print  result,
    # 得到另外一个出现一次的数
    print  result^tmpResult

if  __name__=="__main__":
    arr=[3, 5, 6, 6, 5, 7, 2, 2]
    get2Num(arr)
