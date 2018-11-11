# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:08:48 2018

@author: Administrator
"""

class  EditDistance:
    def  mins(self,a,b,c):
        tmp = a if  a < b else  b
        return  tmp if  tmp < c else  c
    # 参数replaceWight用来表示替换操作与插入删除操作相比的倍数
    def  edit(self,s1,s2,replaceWight):
        # 两个空串的编辑距离为0
        if  s1 == None and s2 == None:
            return  0
        # 如果s1为空串，那么编辑距离为s2的长度
        if  s1 == None:
            return  len(s2)
        if  s2 == None:
            return  len(s1)
        len1 = len(s1)
        len2 = len(s2)
        # 申请二维数组来存储中间的计算结果
        D =[([None]*(len2 +1))  for  i  in  range(len1+1)]
        i=0
        while  i<len1+1:
            D[i][0] = i
            i +=1
        i=0
        while  i < len2+1:
            D[0][i] = i
            i +=1
        i=1
        while  i<len1+1:
            j=1
            while  j<len2+1:
                if  list(s1)[i-1] == list(s2)[j - 1]:
                    D[i][j] = self.mins(D[i - 1][j] + 1, D[i][j - 1] + 1,\
                     D[i -1][j - 1])  #书中错位
                else:
                    D[i][j] = min(D[i-1][j] + 1, D[i][j - 1] + 1, D[i - 1][j -1]\
                     + replaceWight)  #书中印刷错位
                j +=1
            i +=1

        print  "-----------------------------"
        i=0
        while  i<len1+1:
            j=0
            while  j<len2+1:
                print  D[i][j], 
                j +=1
            print  '\n'
            i +=1
        print  "-----------------------------"
        dis = D[len1][len2]
        return  dis

if  __name__=="__main__":
    s1 = "bciln"
    s2 = "fciling"
    ed =EditDistance()
    print  "第一问 : " 
    print  "编辑距离：" + str(ed.edit(s1, s2,1))
    print  "第二问 : "
    print  "编辑距离：" + str(ed.edit(s1, s2,2) )

