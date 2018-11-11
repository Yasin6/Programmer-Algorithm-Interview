# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:16:45 2018

@author: Administrator
"""

def  findMin(array):
    if  array==None or  len(array)<=0:
        print  "输入参数不合理";
        return  0;
    lens=len(array)
    # 数组中没有负数
    if  array[0]>=0:
        return  array[0];
    # 数组中没有正数
    if  array[lens-1]<=0:
        return  array[lens-1];	
    mid = 0;
    begin = 0;
    end = lens - 1;
    absMin = 0;
    # 数组中既有正数又有负数
    while  True:
        mid = begin + (end - begin) / 2;
        # 如果等于0，那么就是绝对值最小的数
        if  array[mid] == 0:
            return  0;   # 如果大于0，正负数的分界点在左侧
        elif  array[mid] > 0:
            # 继续在数组的左半部分查找
            if  array[mid - 1] > 0:
                end = mid - 1;
            elif  array[mid - 1] == 0:
                return  0;
            # 找到正负数的分界点
            else:
                break;#  如果小于0，在数组右半部分查找
        else:
            # 在数组右半部分继续查找
            if  array[mid + 1] < 0:
                begin = mid + 1
            elif  array[mid + 1] == 0:
                return  0;
            # 找到正负数的分界点
            else:
                break;
    # 获取正负数分界点处绝对值最小的值
    if  (array[mid] > 0):
        if  array[mid] < abs(array[mid - 1]):
            absMin = array[mid];
        else:
            absMin = array[mid - 1];
    else: 
        if  abs(array[mid]) < array[mid + 1]:
            absMin = array[mid];
        else:
            absMin = array[mid + 1];            
    return  absMin;

if  __name__=="__main__":
    arr= [-10, -5, -2, 7, 15, 50]
    print  "绝对值最小的数为："+str(findMin(arr))
