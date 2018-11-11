# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:35:25 2018

@author: Administrator
"""

import  random

"""
方法功能：总共n个房间，判断用指定的策略是否能拿到最多金币
返回值：如果能拿到返回True，否则返回False
"""
def  getMaxNum(n):
    if  n<1:
        print  "参数不合法"
        return  
    a = [None]*n
    # 随机生成n个房间里金币的个数
    i=0
    while  i<n:
        a[i] = random.uniform(1,n)  # 生成1～n的随机数
        i +=1
        # 找出前四个房间中最多的金币个数
    max4 = 0
    i=0
    while  i<4:
        if  a[i]>max4:
            max4 = a[i]
        i +=1
    i=4
    while  i<n-1:
        if  a[i]>max4: # 能拿到最多的金币
            return  True
        i +=1
    return  False # 不能拿到最多的金币

if  __name__=="__main__":  
    monitorCount = 1000+0.0
    success = 0
    i=0
    while  i<monitorCount:
        if  getMaxNum(10):
            success +=1
        i +=1
    print  success/monitorCount  

