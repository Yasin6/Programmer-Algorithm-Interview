# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:19:22 2018

@author: Administrator
"""

def  divide(m,n):
    print  str(m)+ "除以" + str(n),
    result = 0
    while  m >= n:
        multi = 1
        # multi * n>m/2(即2* multi * n >m)时结束循环
        while  multi * n <= (m >> 1):
            multi <<= 1
        result += multi
        # 相减的结果进入下次循环
        m -= multi * n    
    print  "商为：" + str(result) + " 余数：" + str(m)

if  __name__=="__main__":
    m = 14  
    n = 4  
    divide(m,n)
