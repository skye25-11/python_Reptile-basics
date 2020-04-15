#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 0031 12:28
# @Author  : skye
# @Site    : 
# @File    : 查找文档元素.py
# @Software: PyCharm
from bs4 import BeautifulSoup
doc='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story"> 
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tilcie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p> 
</body>
</html>
'''
soup=BeautifulSoup(doc,"lxml")
print('1')
tag=soup.find("title")#查找title元素
print(type(tag),tag)
print('-'*50)

print('2')
tags=soup.find_all("a")#查找所有的<a>元素超链接
for tag in tags:
    print(tag)
    print(tag["href"])#获取元素中的内容
    print(tag.text)#查找元素的文本
print('-'*50)

print('3')
tag=soup.find("a")#查找第一个<a>元素
print(tag)
print('-'*50)

print('4')
tag=soup.find("p",attrs={"class":"title"})#查找class=“title”的<p>元素
print(tag)
print('-'*50)

print('5')
tags=soup.find_all(name=None,attrs={"class":"sister"})#name=None表示无论什么名字的元素
for tag in tags:
    print(tag)
print('-'*50)

print('6')
tags=soup.find_all("p")
for tag in tags:
    print(tag.text)
print('-'*50)

print('7')
print('高级查找')
print('通过函数查找复杂节点，查找文本值以“cie”结尾所有<a>节点')
def endsWithWith(s,t):#一个判断结尾内容的函数
    if len(s)>=len(t):
        return s[len(s)-len(t):]==t
    return False
def myFilter(tag):
    return (tag.name=="a"and endsWithWith(tag.text,"cie"))
tags=soup.find_all(myFilter)
for tag in tags:
    print(tag)