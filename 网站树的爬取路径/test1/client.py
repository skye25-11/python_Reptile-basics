#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 0010 18:06
# @Author  : skye
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import urllib.request
from bs4 import BeautifulSoup

def spider(url):
    try:
        data = urllib.request.urlopen(url)
        data = data.read()
        data = data.decode()
        soup = BeautifulSoup(data, "lxml")
        print(soup.find("h3").text)
        links = soup.select("a")
        for link in links:
            href = link["href"]
            url = start_url + "/" + href
            spider(url)
    except Exception as err:
        print(err)
start_url="http://127.0.0.1:5000"
spider(start_url)
print("The End")