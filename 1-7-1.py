# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:29:19 2018

@author: Administrator
"""

class  LNode:  
    def  __new__(self,x):  
        self.data=x 
        self.next=None 

# 把链表相邻元素翻转  
def  reverse (head):
    #判断链表是否为空
    if   head == None or head.next == None:
        return
    cur = head.next # 当前遍历结点
    pre = head # 当前结点的前驱结点
    next = None # 当前结点后继结点的后继结点
    while  cur != None and cur.next != None:
        next = cur.next.next # 见图第（1）步
        pre.next = cur.next # 见图第（2）步
        cur.next.next = cur # 见图第（3）步
        cur.next = next # 见图第（4）步
        pre = cur # 见图第（5）步
        cur = next # 见图第（6）步

if  __name__=="__main__":

    i=1
    head =LNode()
    head.next = None
    tmp = None
    cur = head
    while  i<8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1	
    print  "顺序输出：",
    cur = head.next
    while  cur != None:
        print  cur.data,
        cur = cur.next
    reverse (head)
    print  "\n逆序输出：",
    cur = head.next
    while  cur != None:
        print  cur.data,
        cur = cur.next
    cur = head.next
    while  cur != None:
        cur = cur.next
