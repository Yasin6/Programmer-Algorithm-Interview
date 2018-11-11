# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:07:20 2018

@author: Administrator
"""

# Trie树的结点
class  TrieNode:
    def  __init__(self):
        CHAR_COUNT=11
        self.isLeaf=False
        self.url=None
        self.child=[None]*CHAR_COUNT   # TrieNode[CHAR_COUNT] # CHAR_COUNT
        i=0
        while  i<CHAR_COUNT:
            self.child[i]=None
            i +=1

def  getIndexFromChar(c):
    return  10 if c == '.' else (ord(c) - ord('0'))

def  getCharFromIndex(i):
    return  '.'  if  i==10  else  ('0' + str(i))

class  DNSCache:
    def  __init__(self):
        self.CHAR_COUNT=11     # IP地址最多有11个不同的字符
        self.root =TrieNode() # IP地址最大的长度
    def  insert(self,ip,url):
        # IP地址的长度
        lens = len(ip)
        pCrawl = self.root
        level=0
        while  level<lens:
            # 根据当前遍历到的IP中的字符，找出子结点的索引
            index = getIndexFromChar(ip[level])
            # 如果子结点不存在，则创建一个
            if  pCrawl.child[index] ==None:
                pCrawl.child[index] = TrieNode()
            # 移动到子结点 */
            pCrawl = pCrawl.child[index]
            # 在叶子结点中存储IP对应的URL
            pCrawl.isLeaf = True
            pCrawl.url = url
            level +=1
    # 通过IP地址找到对应的URL
    def  searchDNSCache(self,ip):
        pCrawl = self.root
        lens = len(ip)
        # 遍历IP地址中所有的字符
        level=0
        while  level<lens:
            index = getIndexFromChar(ip[level])
            if  pCrawl.child[index] ==None:
                return  None
            pCrawl = pCrawl.child[index]
            level +=1
        # 返回找到的URL
        if  pCrawl!=None and pCrawl.isLeaf:
            return  pCrawl.url
        return  None

if  __name__=="__main__":
    ipAdds=["10.57.11.127", "121.57.61.129","66.125.100.103"]
    url =["www.samsung.com", "www.samsung.net","www.google.in"]
    n = len(ipAdds)
    cache=DNSCache()
    for  i  in  range(n):
        cache.insert(ipAdds[i],url[i])
        i +=1
    ip = "121.57.61.129"
    res_url = cache.searchDNSCache(ip)
    if  res_url != None:
        print  "找到了IP对应的URL:\n"+ ip+"--->"+ res_url
    else:
        print  "没有找到对应的URL\n"
