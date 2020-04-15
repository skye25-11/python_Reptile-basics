#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 0031 10:45
# @Author  : skye
# @Site    : 
# @File    : First_HTML.py
# @Software: PyCharm
from bs4 import BeautifulSoup
doc='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story"> 
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p> 
</body>
</html>
'''
soup=BeautifulSoup(doc,"lxml")
s=soup.prettify()
print(s)
