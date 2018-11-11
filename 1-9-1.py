# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:30:27 2018

@author: Administrator
"""

class  LNode:  
    def  __new__(self,x):  
        self.data=x 
        self.next=None 

# 方法功能：构造链表 
def  ConstructList(start):
    i=start
    head=LNode()
    head.next=None
    tmp=None
    cur=head
    while  i<7:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i +=2 
    return  head
	
def  PrintList(head):
    cur=head.next
    while  cur!=None:
        print  cur.data,
        cur=cur.next

"""
方法功能：合并两个升序排列的单链表
输入参数：head1与head2代表两个单链表

返回值：合并后链表的头结点
"""
def  Merge(head1,head2):
    if  head1==None or head1.next==None:
        return  head2
    if  head2==None or head2.next==None:
        return  head1
    cur1=head1.next # 用来遍历head1
    cur2=head2.next # 用来遍历head2
    head=None  # 合并后链表的头结点
    cur=None # 合并后的链表在尾结点
    # 合并后链表的头结点为第一个结点元素最小的那个链表的头结点
    if  cur1.data > cur2.data:
        head=head2
        cur=cur2
        cur2=cur2.next
    else:
        head=head1
        cur=cur1
        cur1=cur1.next        
    # 每次找链表剩余结点的最小值对应的结点连接到合并后链表的尾部
    while  cur1!=None and  cur2!=None:
        if  cur1.data < cur2.data:
            cur.next=cur1
            cur=cur1
            cur1=cur1.next
        else:
            cur.next=cur2
            cur=cur2
            cur2=cur2.next
    # 当遍历完一个链表后把另外一个链表剩余的结点链接到合并后的链表后面
    if  cur1!=None:
        cur.next=cur1
    if  cur2!=None:
        cur.next=cur2
    return  head
	
if  __name__=="__main__":
    head1=ConstructList(1)
    head2=ConstructList(2)
    print  "head1: ",
    PrintList(head1)
    print  "\nhead2: ",
    PrintList(head2)
    print  "\n合并后的链表：",
    head=Merge(head1,head2)
    PrintList(head)
