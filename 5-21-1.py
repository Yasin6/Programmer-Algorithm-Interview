# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:14:34 2018

@author: Administrator
"""

# 判断字符c是否是中文字符，如果是返回True
def  isChinese(c):
    return  True if  c >= u'\u4e00' and c<=u'\u9fa5' else False

def  truncateStr(strs,lens):
    if  (strs == None or strs=="" or lens == 0):
        return  ""
    #chrArr = list(strs)
    chrArr=strs
    sb =""
    count = 0  # 用来记录当前截取字符的长度
    for  cc  in  chrArr:
        if  (count < lens):

            #print  sb,count
            if  (isChinese(cc)):
                # 如果要求截取子串的长度只差1个或者2个字符，但是接下来的字符是中文，
                #那么截取结果子串中不保存这个中文字符
                if  count + 1 <= lens and count + 3 >lens :
                    return  sb
                count = count + 3
                sb = sb+cc
            else:
                count = count + 1
                sb = sb+cc
        else:
            break
    return  sb

if  __name__=="__main__":
    sb = "人ABC们DEF"
    sb_unicode=unicode(sb,'utf8')  # 转成unicode编码
    print  truncateStr(sb_unicode, 6)
