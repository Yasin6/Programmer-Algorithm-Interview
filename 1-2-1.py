# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:24:08 2018

@author: Administrator
"""

class  LNode:  
    def  __new__(self,x):  
        self.data=x 
        self.next=None 

"""
** 方法功能：对带头结点的无序单链表删除重复的结点 
** 输入参数：head:链表头结点
"""
def  removeDup(head):
    if  head == None or head.next == None:
        return
    outerCur = head.next  # 用于外层循环，指向链表第一个结点
    innerCur = None  # 用于内层循环用来遍历outerCur后面的结点
    innerPre = None  # innerCur的前驱结点
    while  outerCur != None:
        innerCur = outerCur.next
        innerPre = outerCur
        while  innerCur != None:
            # 找到重复的结点并删除
            if  outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next
        outerCur = outerCur.next

if  __name__=="__main__":
    i = 1
    head =LNode()
    head.next = None
    tmp = None
    cur = head
    while  i<7:
        tmp =LNode()
        if  i % 2 == 0:
            tmp.data = i + 1
        elif   i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i +=1

    print  "删除重复结点前：",
    cur = head.next
    while  cur != None:
        print  cur.data,
        cur = cur.next
    removeDup(head)
    print  "\n删除重复结点后：",
    cur = head.next
    while  cur != None:
        print  cur.data,
        cur = cur.next
