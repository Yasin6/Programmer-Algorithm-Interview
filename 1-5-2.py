# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:27:18 2018

@author: Administrator
"""

# 引申：如何将单链表向右旋转k个位置
class  LNode:  
    def  __new__(self,x):  
        self.data=x 
        self.next=None 

# 方法功能：把链表右旋k个位置 
def  RotateK(head,k):

    if  head==None or head.next==None:
          return  
    # fast指针先走k步，然后与slow指针同时向后走
    slow,fast,tmp=LNode(),LNode(),LNode()
    slow,fast=head.next,head.next
    i=0
    while  i<k and fast!=None: #前移k步
       fast=fast.next
       i +=1   
    # 判断k是否已超出链表长度
    if  i<k:
        return  
    # 循环结束后slow指向链表倒数第k+1个元素，fast指向链表最后一个元素
    while  fast.next!=None:
        slow=slow.next
        fast=fast.next
    tmp=slow
    slow=slow.next 
    tmp.next=None  # 如上图（2）
    fast.next=head.next #如上图（3）
    head.next=slow	# 如上图（4）
	
def  ConstructList():
    i=1
    head=LNode()
    head.next=None
    tmp=None
    cur=head	
    # 构造第一个链表
    while  i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i +=1
    return  head
	
# 顺序打印单链表结点的数据 
def  PrintList(head):
    cur=head.next
    while  cur!=None:
        print  cur.data,
        cur=cur.next

if  __name__=="__main__":
    head=ConstructList()
    print  "旋转前：",
    PrintList(head)
    RotateK(head,3)
    print  "\n旋转后: ",
    PrintList(head)

