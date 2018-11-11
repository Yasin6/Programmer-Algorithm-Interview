# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:40:08 2018

@author: Administrator
"""
#有校正
def  printResult(inputs):
    # 用来存储把input的键与值调换后的信息
    reverseInput =dict()
    for  k,v  in  inputs.items():
        reverseInput[v]=k
    start = None
    # 找到起点
    for  k,v  in  inputs.items():
        if  k not in reverseInput:
            start =k
            break
    if  start == None:
        print  "输入不合理"
        return
    # 从起点出发按照顺序遍历路径
    to = inputs[start]
    print  start +  "->" + to ,
    start=to
    to = inputs[to]
    while  to != None:
        print   ", "+start +  "->" + to,
        start = to
        #to = inputs[to]   #书中代码，修改为下面那句
        to = inputs.get(to,None)  

if  __name__=="__main__": 

    inputs = dict()
    inputs["西安"]="成都"
    inputs["北京"]="上海"
    inputs["大连"]= "西安"
    inputs["上海"]="大连"
    printResult(inputs)
