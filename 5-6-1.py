# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:44:09 2018

@author: Administrator
"""

# 对字符数组排序，使得小写字母在前，大写字母在后	
def  ReverseArray(ch):
    lens=len(ch)
    begin = 0
    end = lens -1
    while  begin < end:
        # 正向遍历找到下一个大写字母
        while  ch[begin]>='a' and  ch[end]<='z' and end > begin:
            begin +=1  
        # 逆向遍历找到下一个小写字母
        while  ch[end]>='A' and ch[end]<='Z' and end > begin:
            end -=1
        temp = ch[begin]
        ch[begin] = ch[end]
        ch[end] = temp
		
if  __name__=="__main__":
    ch=list("AbcDef")
    ReverseArray(ch)
    i=0
    while  i<len(ch):
        print  ch[i],
        i +=1
