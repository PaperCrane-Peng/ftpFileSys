# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/6/5 10:53
# Author    : 彭文瑜
# Site      : 
# File      : update.py
# Product   : PyCharm
# Project   : ftpFilesys
# explain   : 文件说明
from PyQt5.QtCore import pyqtSignal,QObject
import os
from FTP.FTP import myFTP




class down_Thread(QObject):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)
    def __init__(self,ftp_tip,down_file,save_file):
        super(down_Thread, self).__init__()
        self.ftp_tip = ftp_tip
        self.down_file = down_file
        self.save_file = save_file
        self.ftp=myFTP()
        self.ftp_connect()


    def ftp_connect(self):
        host = self.ftp_tip[0]  # 获取IP地址框内容
        port = self.ftp_tip[1]  # 获取端口号，注意要转换为int
        usr = self.ftp_tip[2]  # 获取用户名
        pwd = self.ftp_tip[3]  # 获取密码
        try:
            self.ftp.connect(host, port, timeout=10)  # 连接FTP
        except:
            self.update_date.emit("network connect time out")
        try:
            self.ftp.login(usr, pwd)  # 登录FTP
        except:
            self.update_date.emit("username or password error")



    # 处理业务逻辑
    def run(self):
        # self.ftp.dir(self.down_file)
        size = self.ftp.size(self.down_file)
        # print(size)

        if self.down_file==b"" or self.save_file==b"" :
            self.update_date.emit(str("数据为空"))

        try:
            # self.update_date.emit("0%")
            result=self.ftp.retrbinary("RETR %s" % self.down_file, open(self.save_file, 'wb').write,allSize=size,update_sig=self.update_date)
        except Exception as e:

            self.update_date.emit(str("连接中断...ERROR:%s")%e)
            print(str("连接中断。。。ERROR:%s")%e)
            os.unlink(self.save_file)
        else:
            print('Download Success!')


        # self.ftp.quit()

