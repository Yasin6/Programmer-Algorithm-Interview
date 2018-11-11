# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:48:47 2018

@author: Administrator
"""

"""
方法功能：求字符串的next数组
输入参数：p为字符串，nexts为p的next数组
"""
"""
方法功能：求字符串的next数组
输入参数：p为字符串，nexts为p的next数组
"""
def  getNext(p,nexts):
    i=0
    j=-1  
    nexts[0]=-1
    while  i<len(p):
        if  j==-1 or list(p)[i] ==list(p)[j]:
            i +=1
            j +=1
            nexts[i]=j
        else:
            j=nexts[j]  

def  match(s,p,nexts):
    # 检查参数的合理性，s的长度一定不会小于p的长度
    if  s==None or p==None:
        print  "参数不合理"
        return  -1
    slen=len(s)
    plen=len(p)
    # p肯定不是s的子串
    if  slen<plen:
        return  -1
    i = 0
    j = 0
    while  i < slen and j < plen:
        print  "i="+str(i)+","+"j="+str(j)
        if  j==-1 or list(s)[i] == list(p)[j]:
            # 如果相同，那么继续比较后面的字符
            i +=1
            j +=1
        else:
            # 主串i不需要回溯，从next数组中找出需要比较的模式串的位置j
            j=nexts[j]          
    if  j >= plen: # 匹配成功
        return  i-plen 
    return  -1

if  __name__=="__main__":
    s = "abababaabcbab"
    p = "abaabc"
    lens=len(p)
    nexts=[0]*(lens+1)
    getNext(p,nexts)
    print  "nexts数组为："+str(nexts[0]),
    i=1
    while  i<lens-1:
        print  ","+str(nexts[i]),
        i +=1
    print  '\n'
    print  "匹配结果为："+str(match(s,p,nexts))
