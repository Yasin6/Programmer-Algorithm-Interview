# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:09:42 2018

@author: Administrator
"""

def  findDup(array):
    if  None==array:
        return  -1
    slow = 0
    fast = 0
    while  True:
        fast = array[array[fast]] # fast一次走两步
        slow = array[slow]  # slow一次走一步
        if  slow == fast : # 找到相遇点
             break
    fast=0
    while  True:
        fast = array[fast]
        slow = array[slow] 
        if  slow == fast: # 找到入口点
           return  slow
