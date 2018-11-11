# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:26:14 2018

@author: Administrator
"""
#快慢指针法
class  LNode:  
    def  __new__(self,x):  
        self.data=x 
        self.next=None 

# 构造一个单链表 
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
        print(cur.data),
        cur=cur.next

"""
方法功能：找出链表倒数第k个结点
输入参数：head:链表头结点
返回值：倒数第k个结点
"""
def  FindLastK(head,k):
    if  head==None or head.next==None:
        return  head
    slow=LNode()
    fast=LNode()
    slow=head.next
    fast=head.next
    i=0
    while  i<k and fast!=None:
       fast=fast.next  #前移k步
       i +=1
    if  i<k:

       return  None	
    while  fast!=None:
        slow=slow.next
        fast=fast.next
    return  slow

if  __name__=="__main__":
    head=ConstructList()	# 链表头指针
    result=None
    print  "链表：",
    PrintList(head)
    result=FindLastK(head,3)
    if  result!=None:
        print  "\n链表倒数第3个元素为："+str(result.data),
