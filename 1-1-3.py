# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:22:17 2018

@author: Administrator
"""
#插入法
def  Reverse(head):
    # 判断链表是否为空
       if  head is None or head.next is None:
		  return  
       cur = None #当前结点
       next = None #后继结点
       cur = head.next.next
		# 设置链表第一个结点为尾结点
       head.next.next = None
	   # 把遍历到结点插入到头结点的后面
       while  cur is not  None:
		  next = cur.next
		  cur.next = head.next
		  head.next = cur
		  cur = next


#递归
def  ReversePrint(firstNode):
     if  firstNode is None:
            return
     ReversePrint  (firstNode.next)
     print  firstNode.data,


