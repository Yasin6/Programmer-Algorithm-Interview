# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:30:50 2018

@author: Administrator
"""

class  LNode:  
    def  __new__(self,x):  
        self.data=x 
        self.next=None 

def  printList(head):
    cur=head.next
    while  cur!=None:
        print  cur.data,
        cur=cur.next
		
"""
方法功能：给定单链表中某个结点，删除该结点
输入参数：链表中某结点
返回值： true：删除成功；  false:删除失败
"""
def  RemoveNode(p):
    # 如果结点为空，或结点p无后继结点则无法删除
    if  p==None or p.next==None:
        return  False
    p.data=p.next.data
    tmp=p.next
    p.next=tmp.next
    return  True
	
if  __name__=="__main__":
    i=1
    head=LNode() # 链表头结点
    head.next=None
    tmp=None
    cur=head
    p=None
    # 构造链表
    while  i<8:
        tmp=LNode()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        if  i==5:
            p=tmp
        i +=1
    print  "删除结点"+str(p.data)+"前链表: ",
    printList(head)
    result=RemoveNode(p)
    if  result:
        print  "\n删除该结点后链表:",
        printList(head)
