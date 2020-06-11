# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/6/8 11:58
# Author    : 彭文瑜
# Site      : 
# File      : MyThread.py
# Product   : PyCharm
# Project   : ftpFilesys
# explain   : 文件说明
from PyQt5.QtCore import pyqtSignal,QObject,QThread
import os
from FTP.FTP import myFTP
class MyThread(QThread):

    _signal = pyqtSignal(str)
    # _signal = pyqtSignal(bytes,bytes,socket.socket)
    def __init__(self,target=None,args=(),kwargs=None):
        super(MyThread, self).__init__()
        self._target = target
        # self._signal = pyqtSignal(bytes)
        self._args = args
        if kwargs is None:
            kwargs = {}
        self._kwargs = kwargs

    # 重写run函数，实现线程的工作
    def run(self):
        try:
            if self._target:
                self._target(self._signal,*self._args, **self._kwargs,)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

