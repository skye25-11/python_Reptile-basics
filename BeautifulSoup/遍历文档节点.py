#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 0031 20:02
# @Author  : skye
# @Site    : 
# @File    : 遍历文档节点.py
# @Software: PyCharm
from bs4 import BeautifulSoup
doc='''
<html><head><title>The Dormouse's story</title></head> 
<body> 
<p class="title"><b>The <i>Dormouse's</i> story</b> Once upon a time ...</p>
</body> 
</html> 
'''
print('1')
soup=BeautifulSoup(doc,"lxml")
tag=soup.find("p")#<p>节点的父节点
print(tag.parent.name)
for c in tag.children: #<p>的子节点
    print('<p>的子节点:',c)
    print('<p>的子节点名',c.name)
print('-'*50)

print('2')
tag=soup.find("p")#<p>的子孙节点
for c in tag.descendants:
    print(c)
print('-'*50)

print('3')
tag=soup.find("b")#<b>的兄弟节点
print(tag.next_sibling)#tag.next_sibling 是 <b> 的临近的下一个兄弟节点
print(tag.previous_sibling)#tag.previous_sibling 是 tag 的临近的前一个兄弟节
