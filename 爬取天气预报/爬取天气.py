#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 0001 10:06
# @Author  : skye
# @Site    : 
# @File    : 爬取天气预报.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
url="http://www.weather.com.cn/weather/101281701.shtml"
try:
    #模拟浏览器
    headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
    req=urllib.request.Request(url,headers=headers)
    data=urllib.request.urlopen(req)#获取二进制
    data=data.read()
    dammit = UnicodeDammit(data, ["utf-8", "gbk"])
    data = dammit.unicode_markup#转为unicode编码
    soup = BeautifulSoup(data, "lxml")
    #地区
    tags = soup.select("div[class='ctop clearfix'] div")
    for tag in tags:
        print(tag.text)
    lis = soup.select("ul[class='t clearfix'] li")
    n=0
    for li in lis:
        try:
            data=li.select('h1')[0].text
            weather=li.select('p[class="wea"]')[0].text
            if n>0:
                temp=li.select('p[class="tem"] span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
            else:
                temp = li.select('p[class="tem"] i')[0].text
            fengxiang=li.select('p[class="win"] span')[0]
            fengji=li.select('p[class="win"] i')[0].text
            print(data,weather,temp,fengxiang["title"],fengji)
            n=n+1
        except Exception as err:
            print(err)
except Exception as err:
    print(err)
