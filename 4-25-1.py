# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:28:40 2018

@author: Administrator
"""

"""
param t    每个服务器处理的时间
param n    任务的个数
return      各个服务器执行完任务所需的时间
"""
def  calculate_process_time(t,n):
    if  t==None or n<=0:
        return  None
    m=len(t)
    proTime=[0]*m
    i=0
    while  i<n:
        minTime = proTime[0] + t[0]  # 把任务给第j个机器上后这个机器的执行时间
        minIndex = 0                 # 把任务给第minIndex个机器上
        j=1
        while  j<m:
            # 分配到第j台机器上后执行时间更短
            if  minTime > proTime[j] + t[j]:
                minTime = proTime[j] + t[j]
                minIndex = j
            j +=1
        proTime[minIndex] += t[minIndex]
        i +=1
    return  proTime

if  __name__=="__main__":
    t=[7,10]
    n =6
    proTime= calculate_process_time(t,n)
    if  proTime==None:
        print  "分配失败"
    else: 	
        totalTime=proTime[0]
        i=0
        while  i < len(proTime):
            print  "第" + str((i + 1)) + "台服务器有" + str(proTime[i] / t[i])	+ "个任务,执行总时间为：" + str(proTime[i])
            if  proTime[i]>totalTime:
                totalTime=proTime[i]
            i +=1
        print   "执行完所有任务所需的时间为" + str(totalTime)
