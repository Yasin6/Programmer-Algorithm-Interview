# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:42:54 2018

@author: Administrator
"""

def  isContain(str1,str2): 
    len1 = len(str1)
    len2 = len(str2)
    # 字符串ch1比ch2短
    if  len1 < len2:
        i=0
        while  i<len1:
            j=0
            while  j<len2:
                if  list(str1)[i] == list(str2)[j]:
                    break
                j +=1
            if  (j >= len2):
                return  False
            i +=1
    else:
        # 字符串ch1比ch2长
        i=0
        while  i < len2:
            j=0
            while  j < len1:
                if  (list(str1)[j] == list(str2)[i]):
                    break
                j +=1
            if  j >= len1:
                    return  False
            i +=1
    return  True

if  __name__=="__main__":
    str1 = "abcdef"
    str2 = "acf"
    isContain = isContain(str1, str2)
    print  str1 + "与" + str2,
    if  (isContain):
        print  "有包含关系"
    else:
        print  "没有包含关系"
