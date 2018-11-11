# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:12:56 2018

@author: Administrator
"""

def  get2Num(arr):
    if  arr==None or len(arr)<1:
        print  "参数不合理"
        return
    dic=dict()
    i=0
    while  i <len(arr):
        # dic中没有这个数字，说明第一次出现，value赋值为1
        if  arr[i] not in dic:
            dic[arr[i]]=1
        # 当前遍历的值在dic中存在，说明前面出现过，value赋值为0
        else:
            dic[arr[i]]=0
        i +=1
    for  k,v  in  dic.items():
         if  v==1:
             print  int(k)
	
if  __name__=="__main__":
    arr=[3, 5, 6, 6, 5, 7, 2, 2]
    get2Num(arr)
