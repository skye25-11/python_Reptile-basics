#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 0001 9:33
# @Author  : skye
# @Site    : 
# @File    : css查找2.py
# @Software: PyCharm
from bs4 import BeautifulSoup
doc="<div><p>A</p><span><p>B</p></span></div><div><p>C</p></div>"
soup=BeautifulSoup(doc,"lxml")
tags=soup.select("div p")#是查找<div>下面的所有子孙节点<p>，因此包含<span>下面 的<p>B</p>。
for tag in tags:
    print(tag)
print('-'*50)

tags=soup.select("div > p")#查找<div>下面的直接子节点<p>，因此不包含<span>下 面的<p>B</p>。
for tag in tags:
    print(tag)
print('-'*50)


