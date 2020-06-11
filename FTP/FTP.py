# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/6/5 15:44
# Author    : 彭文瑜
# Site      : 
# File      : FTP.py
# Product   : PyCharm
# Project   : ftpFilesys
# explain   : 文件说明
from ftplib import FTP

try:
    import ssl
except ImportError:
    _SSLSocket = None
else:
    _SSLSocket = ssl.SSLSocket
class myFTP(FTP):
    def __init__(self):
        super(myFTP, self).__init__()

    def retrbinary(self, cmd, callback, blocksize=8192, rest=None,allSize=0,update_sig=None):
        """Retrieve data in binary mode.  A new port is created for you.

        Args:
          cmd: A RETR command.
          callback: A single parameter callable to be called on each
                    block of data read.
          blocksize: The maximum number of bytes to read from the
                     socket at one time.  [default: 8192]
          rest: Passed to transfercmd().  [default: None]
          allSize：整个图片的大小
        update_sig：关联的信号，用于更新主窗口
        Returns:
          The response code.
        """
        self.voidcmd('TYPE I')
        long=0
        with self.transfercmd(cmd, rest) as conn:
            while 1:
                data = conn.recv(blocksize)
                long += len(data)

                if not data:
                    break
                callback(data)
                if update_sig is not None:
                    update_sig.emit(str(int(float(long / allSize)*100)) + "%")
                    # print(long,allSize,int(float(long / allSize)*100))
            # shutdown ssl layer
            if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                conn.unwrap()
        return self.voidresp()