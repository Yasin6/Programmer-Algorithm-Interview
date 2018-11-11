# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:15:13 2018

@author: Administrator
"""

def  getRelativePath(path1,path2):
    if  path1 == None  or path2 == None:
        print  "参数不合法\n"
        return  
    relativePath = ""
    # 用来指向两个路径中不同目录的起始路径
    diff1 = 0
    diff2 = 0
    i=0
    j=0
    len1 = len(path1)
    len2 = len(path2)
    while  i<len1 and j<len2:
        # 如果目录相同，那么往后遍历
        if  list(path1)[i] == list(path2)[j]:
            if  list(path1)[i] == '/':
                diff1 = i
                diff2 = j
            i +=1
            j +=1
        else:
            # 不同的目录
            # 把path1非公共部分的目录转换为../
            diff1 +=1  # 跳过目录分隔符/
            while  diff1<len1:
                # 碰到下一级目录
                if  list(path1)[diff1] == '/':
                    relativePath+="../"
                diff1 +=1
            # 把path2的非公共部分的路径加到后面
            diff2 +=1
            relativePath += path2[diff2:]
            break
    return  relativePath

if  __name__=="__main__":
    path1 = "/qihoo/app/a/b/c/d/new.c"
    path2 = "/qihoo/app/1/2/test.c"
    print  getRelativePath(path1,path2)
