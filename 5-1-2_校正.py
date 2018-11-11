# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:31:43 2018

@author: Administrator
"""

# 交换字符数组下标为i和j对应的字符  
def  swap(str,i,j):
    tmp=str[i]
    str[i]=str[j]
    str[j]=tmp

"""
方法功能：翻转字符串
输入参数：begin与end分别为字符串的第一个字符与最后一个字符的下标
"""

def  Reverse(str,begin,end):
    i=begin
    j=end
    while  i<j:
        swap(str,i,j)
        i +=1
        j -=1

"""
方法功能：根据当前字符串的组合
输入参数：str：字符数组
返回值：还有下一个组合返回True，否则返回False
"""
def  getNextPermutation(str):
    end = len(str) - 1 # 字符串最后一个字符的下标
    cur = end  # 用来从后向前遍历字符串
    suc = 0 # cur的后继
    tmp = 0  
    while  cur != 0:
        # 从后向前开始遍历字符串
        suc = cur  
        cur -=1
        if  str[cur] < str[suc]:
            # 相邻递增的字符，cur指向较小的字符
            # 找出cur后面最小的字符tmp  
            tmp = end
            while  str[tmp] < str[cur]:
                tmp -=1
            # 交换cur与tmp
            swap(str,cur ,tmp)
            # 把cur后面的子字符串进行翻转
            Reverse(str,suc , end)  
            return  True  
    return  False

"""
方法功能：获取字符串中字符的所有组合
输入参数：str:字符数组
"""
def  Permutation (s):
    if  s==None or len(s)<1:
        print  "参数不合法"
        return
    str=list(s)
    str.sort() # 升序排列字符数组
    print  str
    print  ''.join(str),
    while  getNextPermutation(str):
        print  ''.join(str), 
	
if  __name__=="__main__":  #书中等号之间有空格
    s = "abc"  
    Permutation(s)
