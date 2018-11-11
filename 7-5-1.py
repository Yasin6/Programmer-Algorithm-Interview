# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:36:36 2018

@author: Administrator
"""

import  random
def  getRandomM(a,n,m):
    if  a==None or n<=0 or n<m:
        print  "参数不合理"
        return
    i=0
    while  i<m: 
        j=random.randint(i,n-1) # // 获取i到n-1间的随机数
        # 随机选出的元素放到数组的前面
        tmp=a[i]
        a[i]=a[j]
        a[j]=tmp 
        i +=1

if  __name__=="__main__":   
    a= [1, 2, 3, 4, 5, 6, 7, 8, 9,10 ]
    n = 10
    m = 6  
    getRandomM(a, n, m)
    i=0
    while  i<m:
        print  a[i],
        i +=1
