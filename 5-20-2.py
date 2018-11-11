# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:13:59 2018

@author: Administrator
"""

def  getMinPath(arr) :
    if  arr == None or len(arr) ==0:
        return  0 
    row = len(arr)
    col = len(arr[0])   
    # 用来保存计算的中间值
    cache =[([None]*col)  for  i  in  range(row)]
    cache[0][0] = arr[0][0]    	
    i=1
    while  i<col:
        cache[0][i] = cache[0][i-1] + arr[0][i]
        i +=1
    j=1
    while  j<row:
        cache[j][0] = cache[j-1][0] + arr[j][0]
        j +=1        
    # 在遍历二维数组的过程中不断把计算结果保存到cache中
    print"路径:",
    i=1
    while  i<row:
        j=1
        while  j<col:
            # 可以确定选择的路线为arr[i][j-1]
            if  cache[i-1][j] > cache[i][j-1]:
                cache[i][j] = cache[i][j-1] + arr[i][j]
                print  "["+str(i)+","+str(j-1)+"]  ",
            #可以确定选择的路线为arr[i-1][j]
            else:
                cache[i][j] = cache[i-1][j] + arr[i][j]
                print  "["+str(i-1)+","+str(j)+"]  ",
            j +=1
        i +=1 
    print("["+str(row-1)+","+str(col-1)+"]")
    return  "最小值为："+str(cache[row-1][col-1])

if  __name__=="__main__":
    arr =[[1, 4, 3],[8, 7, 5],[2, 1, 5]] 
    print  getMinPath(arr)
