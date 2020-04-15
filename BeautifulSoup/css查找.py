#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 0001 8:58
# @Author  : skye
# @Site    : 
# @File    : css查找.py
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
<a href="http://example.com/tilsie" class="sister" id="link3">Tilsie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p> 
</body>
</html>
'''
soup=BeautifulSoup(doc,"lxml")
tags=soup.select("p[class='story'] a")#查找<p>节点下有class='story'的所有<a>节点
for tag in tags:
    print(tag["href"])
print('-'*50)

tags=soup.select("a[href='http://example.com/elsie']")#soup.select("a[href='http://example.com/elsie']") 查找 href="http://example.com/elsie"的<a> 节点；
for tag in tags:
    print(tag["href"])
print('-'*50)

tags=soup.select("a[href$='sie']")# soup.select("a[href$='sie']") 查找 href 以"sie"结尾的<a>节点；
for tag in tags:
    print(tag["href"])
    print(tag.text)#查找 href 以"sie"结尾的<a>文本节点；
print('-'*50)

tags=soup.select("a[href^='http://example.com']")# soup.select("a[href^='http://example.com']") 查找href以"http://example.com"开始的<a>节 点；
for tag in tags:
    print(tag["href"])
print('-'*50)

tags=soup.select("a[href*='example']")# soup.select("a[href*='example']") 查找 href 的值中包含"example"字符串的<a>节点;
for tag in tags:
    print(tag["href"])
print('-'*50)
