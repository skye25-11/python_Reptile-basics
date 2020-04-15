#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 0015 9:08
# @Author  : skye
# @Site    : 
# @File    : 基础.py
# @Software: PyCharm
import requests
r =requests.get("http://www.baidu.com")
print(r.status_code)
print("-"*50)
print(r.text)
print("-"*50)
print(r.encoding)
print("-"*50)
print(r.apparent_encoding)
print("-"*50)
r.encoding="utf-8"
print(r.text)



