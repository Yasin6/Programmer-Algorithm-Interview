# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:32:04 2018

@author: Administrator
"""

"""
方法功能：处理数字相加的进位
输入参数：num为字符数组，pos为进行加1操作对应的下标位置
"""
def  carry(num,pos):
    while  pos>0:
        if  int(num[pos])>9:
            num[pos]='0'
            num[pos-1]=str(int(num[pos-1]) + 1)
        pos -=1
	
"""
方法功能：获取大于n的最小不重复数
输入参数：n为正整数
返回值：大于n的最小不重复数
"""
def  findMinNonDupNum(n):
    count=0 # 用来记录循环次数
    nChar=list(str(n+1))
    ch=[None]*(len(nChar)+2)
    ch[0]='0'
    ch[len(ch)-1]='0'
    i=0
    while  i<len(nChar):
        ch[i+1]=nChar[i]
        i +=1
    lens=len(ch)
    i=lens-2 # 从右向左遍历
    while  i>0:
        count +=1
        if  ch[i-1] ==ch[i]:
            ch[i]=str(int(ch[i]) +1) #末尾数字加1 
            carry(ch,i) # 处理进位
            # 把下标为i后面的字符串变为0101…串
            j=i+1
            while  j<lens:
                if  (j-i)%2==1 :
                    ch[j]='0'
                else:
                    ch[j]='1'
                j +=1
            # 第i位加1后，可能会与第i+1位相等
            i +=1
        else:
            i -=1
    print  "循环次数为："+str(count)
    return  int(''.join(ch))

if  __name__=="__main__":
    print  findMinNonDupNum(23345)
    print  findMinNonDupNum(1101010)
    print  findMinNonDupNum(99010)
    print  findMinNonDupNum(8989)

