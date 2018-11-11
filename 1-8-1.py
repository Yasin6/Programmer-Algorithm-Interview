# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:29:49 2018

@author: Administrator
"""

class  LNode:  

    def  __new__(self,x):  
        self.data=x 
        self.next=None 

# 对不带头结点的单链表翻转 
def  Reverse(head):
    if  head==None or head.next==None:
        return  head
    pre=head # 前驱结点
    cur=head.next # 当前结点
    next=cur.next # 后继结点
    pre.next=None   
    # 使当前遍历到的结点cur指向其前驱结点
    while  cur!=None:
        next=cur.next
        cur.next=pre
        pre=cur
        cur=cur.next	
        cur=next       
    return  pre
	
# 对链表K翻转 
def  ReverseK(head,k):
    if  head==None or head.next==None or k<2:
        return  
    i=1
    pre=head
    begin=head.next
    end=None
    pNext=None    
    while  begin!=None:
        end=begin
        # 对应图中第(1)步，找到从begin开始第K个结点
        while  i<k:
            if  end.next!=None:
                end=end.next
            else:    # 剩余结点的个数小于K
                return  
            i +=1
        pNext=end.next # (2)
        end.next=None  # (3)
        pre.next=Reverse(begin)  # (4) (5)
        begin.next=pNext  # (6)
        pre=begin # (7)
        begin=pNext # (8)
        i=1

if  __name__=="__main__":
    i=1

    head=LNode()

    head.next=None
    tmp=None
    cur=head	
    while  i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    print  "顺序输出：",
    cur=head.next
    while  cur!=None:
        print  cur.data,
        cur=cur.next
    ReverseK(head,3)
    print  "\n逆序输出：",
    cur=head.next
    while  cur!=None:
        print  cur.data,
        cur=cur.next
    cur=head.next
    while  cur!=None:
        tmp=cur
        cur=cur.next
