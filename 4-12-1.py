# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:19:02 2018

@author: Administrator
"""

def  rotateArr(arr):
    lens=len(arr)
    # 打印二维数组右上半部分
    i=lens-1
    while  i>0:
        row=0
        col=i
        while  col<lens:
            print  arr[row][col],
            row +=1
            col +=1
        print  '\n'
        i -=1   
    # 打印二维数组左下半部分（包括对角线）
    i=0
    while  i<lens:
        row=i
        col=0
        while  row <lens:
            print  arr[row][col],
            row +=1
            col +=1
        print  '\n'
        i +=1

if  __name__=="__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    rotateArr(arr)

