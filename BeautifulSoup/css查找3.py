#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 0001 9:50
# @Author  : skye
# @Site    : 
# @File    : css查找3.py
# @Software: PyCharm
from bs4 import BeautifulSoup
doc="<body>demo<div>A</div><b>X</b><p>B</p><span><p>C</p></span><p>D</p></div></body>"
soup=BeautifulSoup(doc,"lxml")
print(soup.prettify())
print('-'*50)
tags=soup.select("div ~ p")
for tag in tags:
    print(tag)
print('-'*50)


tags=soup.select("div + b")
for tag in tags:
    print(tag)
