# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:13:34 2018

@author: Administrator
"""

"""
方法功能：在数组array中找出第k小的值
输入参数：array为整数数组，low为数组起始下标，high为数组右边界的下标，k为整数
返回值：数组中第k小的值
"""
def  findSmallK(array,low,high,k):
    i = low  
    j = high  
    splitElem = array[i]  
    # 把小于等于splitElem的数放到数组中splitElem的左边，大于splitElem的值放到右边
    while  i < j:
        while  i < j  and  array[j] >= splitElem:
            j -=1
        if  i < j:
            array[i] = array[j]
            i +=1
        while  i < j and array[i] <= splitElem:
            i +=1  
        if  i < j:
            array[j] = array[i] 
            j -=1
    array[i] = splitElem 
    # splitElem在子数组array[low~high]中下标的偏移量
    subArrayIndex=i-low
    # splitElem在array[low~high]所在的位置恰好为k-1,那么它就是第k小的元素
    if  subArrayIndex==k-1:
        return  array[i]
    # splitElem在array[low~high]所在的位置大于k-1,那么只需在array[low~i-1]中找第k小的元素
    elif  subArrayIndex > k-1:
        return  findSmallK(array, low, i-1, k) 
    # 在array[i+1~high]中找第k-i+low-1小的元素
    else:
        return  findSmallK(array, i+1, high, k-(i-low)-1)  

if  __name__=="__main__":
    k=3
    array=[4, 0, 1, 0, 2, 3]
    print  "第"+str(k)+"小的值为："+str(findSmallK(array,0,len(array)-1,k))
