# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:11:15 2018

@author: Administrator
"""

# python中可以使用列表来表示有序数组，因此示例代码中使用列表来表示有序数组。
def  getMin_1(arr,low,high):
    # 如果旋转个数为0，即没有旋转，单独处理，直接返回数组头元素
    if  high<low:
        return  arr[0]
    # 只剩下一个元素一定是最小值
    if  high == low:
        return  arr[low]
    # mid=(low+high)/2，采用下面写法防止溢出
    mid =low + ((high - low) >> 1)
    # 判断是否arr[mid]为最小值
    if  arr[mid] <arr[mid - 1]:
        return  arr[mid]
    # 判断是否arr[mid + 1]为最小值
    elif  arr[mid + 1] <arr[mid]:
        return  arr[mid + 1]
    # 最小值一定在数组左半部分
    elif  arr[high] >arr[mid]:
        return  getMin(arr, low, mid - 1)
    # 最小值一定在数组右半部分
    elif  arr[mid]>arr[low]:
        return  getMin(arr, mid + 1, high)
    # arr[low] == arr[mid] && arr[high] == arr[mid]
    # 这种情况下无法确定最小值所在的位置，需要在左右两部分分别进行查找
    else:
        return  min(getMin(arr, low, mid - 1), getMin(arr, mid + 1, high))	
	
def  getMin(arr):
    if  None==arr:
        print  "参数不合法"
        return  
    else:
        return  getMin_1(arr,0,len(arr)-1)

if  __name__=="__main__":
    array1=[5, 6, 1, 2, 3, 4]
    mins=getMin(array1)
    print  mins
    array2=[1, 1, 0, 1]
    mins=getMin(array2)
    print  mins
