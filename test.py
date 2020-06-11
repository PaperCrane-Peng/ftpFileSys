# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/6/11 13:13
# Author    : 彭文瑜
# Site      : 
# File      : test.py
# Product   : PyCharm
# Project   : ftpFilesys
# explain   : 文件说明

import time

nowtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
if nowtime[-5:]=="00:00":
    print("%s,线程ID：%d,正常运行")

print(time1)