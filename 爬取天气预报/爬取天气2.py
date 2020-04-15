#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 0007 18:46
# @Author  : skye
# @Site    : 
# @File    : 爬取天气2.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import sqlite3
class WeatherDB:
    def openDB(self):
        self.com= self.con=sqlite3.connect("weathers.db")
        self.cursor=self.con.cursor()
        try:
            self.cursor.execute("create table weathers (wCity varchar(16),\
                                wDate varchar(16),wWeather varchar(64),wTemp varchar(32),\
                                constraint pk_weather primary key (wCity,wDate))")
        except:
            self.cursor.execute("delete from weathers")

    def closeDB(self):
        self.com.commit()
        self.com.close()
    def insert(self,city,date,weather,temp):
        try:
            self.cursor.execute("insert into weathers (wCity,wDate,wWeather,wTemp)\
                                values(?,?,?,?)",
                                (city,date,weather,temp))
        except Exception as err:
            print(err)

    def show(self):
        self.cursor.execute("select * from weathers")
        rows=self.cursor.fetchall()
        print("%-16s%-16s%-32s%-16s" % ("city","date","weather","temp"))
        for row in rows:
            print("%-16s%-16s%-32s%-16s" % (row[0], row[1], row[2], row[3]))

class WeatherForecast:
    def __init__(self):
        self.headers ={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
        self.cityCode={"中山":"101281701","惠州":"101280301","肇庆":"101280901","清远":"101281301","茂名":"101282001"}
    def forecastCity(self, city):
        if city not in self.cityCode.keys():
            print(city + " 找不到代码")
            return
        url = "http://www.weather.com.cn/weather/" + self.cityCode[city] + ".shtml"
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
            req = urllib.request.Request(url, headers=headers)
            data = urllib.request.urlopen(req)  # 获取二进制
            data = data.read()
            dammit = UnicodeDammit(data, ["utf-8", "gbk"])
            data = dammit.unicode_markup  # 转为unicode编码
            soup = BeautifulSoup(data, "lxml")
            lis = soup.select("ul[class='t clearfix'] li")
            for li in lis:
                try:
                    date = li.select('h1')[0].text
                    weather = li.select('p[class="wea"]')[0].text
                    temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
                    print(city,date,weather,temp)
                    self.db.insert(city, date, weather, temp)
                except Exception as err:
                    print(err)
            print('-' * 50)
        except Exception as err:

            print(err)
    def process(self, cities):
        self.db = WeatherDB()
        self.db.openDB()
        for city in cities:
            self.forecastCity(city)
        self.db.closeDB()

ws = WeatherForecast()
ws.process(["中山", "惠州", "肇庆", "清远","茂名"])
print("completed")










