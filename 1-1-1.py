# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:18:14 2018

@author: Administrator
"""

class  LNode:  
    def  __new__(self,x):  
        self.data=x  
        self.next=None  

# 方法功能：对单链表进行逆序 输入参数：head:链表头结点 
def  Reverse(head): 
    # 判断链表是否为空
    if  head == None or head.next == None:


		return
    pre = None  #前驱结点
    cur = None  # 当前结点
    next = None # 后继结点
	#把链表首结点变为尾结点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
	#使当前遍历到的结点cur指向其前驱结点
    while  cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next
    #链表最后一个结点指向倒数第二个结点
    cur.next = pre
	#链表的头结点指向原来链表的尾结点
    head.next = cur
	
if  __name__=="__main__":
    i = 1
	#链表头结点
    head = LNode()
    head.next = None
    tmp = None
    cur = head
	#构造单链表
    while  i<8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1	
    print  "逆序前：",
    cur = head.next
    while  cur != None:
        print  cur.data,
        cur = cur.next
    print  "\n逆序后：",
    Reverse(head)
    cur = head.next
    while  cur != None:
         print  cur.data,
         cur = cur.next
