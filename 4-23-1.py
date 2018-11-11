# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:27:09 2018

@author: Administrator
"""

class  MySet:
     def  __init__(self,mins,maxs): 
         self.mins=mins
         self.maxs= maxs         
     def  getMin(self) : 
         return  self.mins  
     def  setMin(self,mins): 
         self.mins=mins       
     def  getMax(self):
         return  self.maxs   
     def  setMax(self,maxs):
         self.maxs = maxs
	
def  getIntersection(s1,s2):
    if  s1.getMin()<s2.getMin():
        if  s1.getMax()<s2.getMin():
            return  None
        elif  s1.getMax()<=s2.getMax():
            return  MySet(s2.getMin(),s1.getMax())
        else:
				return  MySet(s2.getMin(),s2.getMax())            
    elif  s1.getMin()<=s2.getMax():
        if  s1.getMax()<=s2.getMax():
            return  MySet(s1.getMin(),s1.getMax())
        else:
            return  MySet(s1.getMin(),s2.getMax())
    else:
        return  None
	
def  getIntersection2(l1,l2):
    result=[]
    i=0
    while  i<len(l1):
        j=0
        while  j<len(l2):
            s=getIntersection(l1[i],l2[j])
            if  s!=None:
                result.append(s)
            j +=1
        i +=1
    return  result

if  __name__=="__main__":
    l1=[]
    l2=[]
    l1.append(MySet(4,8))
    l1.append(MySet(9,13))  
    l2.append(MySet(6,12))
    result=getIntersection2(l1,l2)
    i=0
    while  i<len(result):
        print  "["+str(result[i].getMin())+","+str(result[i].getMax()) + "] "
        i +=1
