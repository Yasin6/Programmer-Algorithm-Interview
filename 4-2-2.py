# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:10:54 2018

@author: Administrator
"""

class  MaxMin:
    # 返回值列表中有两个元素，第一个元素为子数组的最小值，第二个元素为最大值
    def  getMaxMin(self,array,l,r):
        if  array==None:
            print  "参数不合法"
            return  
        list=[]
        m = (l + r) / 2 # 求中点
        if  l == r:   # l与r之间只有一个元素
           list.append(array[l])
           list.append(array[l])
           return  list
        if  l + 1 == r:  # l与r之间只有两个元素
           if  array[l] >= array[r]:
               max = array[l]
               min = array[r]
           else:
               max = array[r]
               min = array[l]
           list.append(min)
           list.append(max)
           return  list
        # 递归计算左半部份
        lList=self.getMaxMin(array,l,m)  
        # 递归计算右半部份
        rList=self.getMaxMin(array, m + 1, r) 
        # 总的最大值
        max =lList[1] if  (lList[1]>rList[1]) else  rList[1]
	    # 总的最小值
        min = lList[0] if  (lList[0]<rList[0]) else rList[0]
        list.append(min)
        list.append(max)
        return  list

if  __name__=="__main__":
    array =[7, 3, 19, 40, 4, 7, 1]
    m=MaxMin()
    result=m.getMaxMin(array,0,len(array)-1)
    print   "max=" + str(result[1])
    print   "min=" + str(result[0])
