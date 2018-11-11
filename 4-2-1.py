# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:10:20 2018

@author: Administrator
"""

class  MaxMin:
    def  __new__(self):
        self.max=None
        self.min=None
    def  getMax(self):  return  self.max
    def  getMin(self):  return  self.min  
    def  GetmaxAndmin(self,arr):
        if  arr==None:
            print  "参数不合法"
            return
        i = 0
        lens=len(arr)
        self.max = arr[0]
        self.min = arr[0]        
        # 两两分组，把较小的数放到左半部分，较大的数放到右半部分
        i=0
        while  i < (lens-1):
            if  arr[i] >arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
            i +=2                
        # 在各个分组的左半部分找最小值
        self.min = arr[0]
        i=2
        while  i<lens:
            if  arr[i] <self.min:
                self.min = arr[i]
            i +=2
        # 在各个分组的右半部分找最大值
        self.max = arr[1]
        i=3
        while  i < lens:
            if  arr[i] >self.max:
                self.max = arr[i]
            i +=2        
        # 如果数组中元素个数是奇数个，最后一个元素被分为一组，需要特殊处理
        if  lens % 2 ==1:
            if  self.max<arr[lens - 1]:
                self.max = arr[lens - 1]
            if  self.min > arr[lens-1]:
                self.min=arr[lens-1]

if  __name__=="__main__":
    array =[7,3,19,40,4,7,1]
    m=MaxMin()
    m.GetmaxAndmin(array)
    print  "max=" + str(m.getMax())
    print  "min=" + str(m.getMin())
