# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:48:17 2018

@author: Administrator
"""

"""
方法功能：判断p是否为s的子串，如果是，那么返回p在s中第一次出现的下标，否则返回-1
输入参数：s和p分别为主串和模式串
"""
def  match(s,p):
    # 检查参数的合理性
    if  s==None or  p==None:
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
        if  list(s)[i] == list(p)[j]:
            # 如果相同，那么继续比较后面的字符
            i +=1
            j +=1
        else:
            # 后退回去重新比较
            i = i - j + 1  
            j = 0
            if(i>slen-plen):
                return  -1
    if  j >= plen:  # 匹配成功
        return  i - plen
    return  -1

if  __name__=="__main__":
    s = "xyzabcd"
    p = "abc"
    print  match(s, p)
