# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Python_projects\ftpFilesys\myUI\ftpFilesys.ui'
#
# Created by: PyQt5 myUI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette
class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        # Form.resize(1024, 800)

        # self.widget = Form
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 800, 640))
        self.widget.setObjectName("widget")
        self.setMinimumSize(640,480)
        # 垂直布局
        self.vbox = QtWidgets.QVBoxLayout(self.widget)    # 垂直（Vertical）布局
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName("verticalLayout")

        # 调用布局函数
        self.user_text()
        self.ftp_text()
        self.label_log = QtWidgets.QLabel(self.widget)
        self.label_log.setObjectName("label_log")
        self.label_log.setMaximumHeight(30)

        self.Text_log = QtWidgets.QTextBrowser(self.widget)
        self.Text_log.setObjectName("Text_log")
        self.Text_log.setMaximumHeight(300)
        # 设置整体布局
        # spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        self.vbox.addLayout(self.hbox)
        # self.vbox.addItem(spacerItem)
        self.vbox.addLayout(self.gridLayout_file)
        # self.vbox.addItem(spacerItem)
        self.vbox.addWidget(self.label_log)
        self.vbox.addWidget(self.Text_log)
        self.vbox.setSpacing(20)


        self.widget.setLayout(self.vbox)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Bt_link.setText(_translate("Form", "连接"))
        self.Bt_up.setText(_translate("Form", "上传"))
        self.Bt_down.setText(_translate("Form", "下载"))

        self.label_port.setText(_translate("Form", "端口号"))
        self.label_ip.setText(_translate("Form", "IP地址"))
        self.label_user.setText(_translate("Form", "用户名"))
        self.label_pwd.setText(_translate("Form", "密码"))
        self.label_master.setText(_translate("Form", "FTP目录"))
        self.label_local.setText(_translate("Form", "本地站点"))
        self.label_log.setText(_translate("Form", "日志"))

    # ftp连接信息布局设置
    def user_text(self):
        # ************* 水平布局——连接信息部分
        # 创建水平布局
        self.hbox = QtWidgets.QHBoxLayout(self.widget)  # 水平（Horizontal）布局
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setObjectName("horizontalLayout")

        # 控件创建
        # button 创建
        self.Bt_link = QtWidgets.QPushButton(self.widget)
        self.Bt_link.setObjectName("Bt_link")
        # Edit 创建
        self.lineEdit_ip = QtWidgets.QLineEdit(self.widget)  # ip输入
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lineEdit_port = QtWidgets.QLineEdit(self.widget)  # 端口号输入
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.lineEdit_user = QtWidgets.QLineEdit(self.widget)  # 用户名输入
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget)  # 密码输入
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        # Label 创建
        self.label_port = QtWidgets.QLabel(self.widget)  # 端口号
        self.label_port.setObjectName("label_port")
        self.label_ip = QtWidgets.QLabel(self.widget)  # IP
        self.label_ip.setObjectName("label_ip")
        self.label_user = QtWidgets.QLabel(self.widget)  # 用户名
        self.label_user.setObjectName("label_user")
        self.label_pwd = QtWidgets.QLabel(self.widget)  # 密码
        self.label_pwd.setObjectName("label_pwd")

        # 布局配置
        self.hbox.addWidget(self.label_ip)
        self.hbox.addWidget(self.lineEdit_ip)
        self.hbox.addWidget(self.label_port)
        self.hbox.addWidget(self.lineEdit_port)
        self.hbox.addWidget(self.label_user)
        self.hbox.addWidget(self.lineEdit_user)
        self.hbox.addWidget(self.label_pwd)
        self.hbox.addWidget(self.lineEdit_pwd)
        self.hbox.addWidget(self.Bt_link)
        self.hbox.setSpacing(20)

    # ftp文件系统布局设置
    def ftp_text(self):
        # ************* 水平布局——连接信息部分
        # 创建栅格布局
        self.gridLayout_file = QtWidgets.QGridLayout()
        self.gridLayout_file.setObjectName("gridLayout_file")
        # button 创建
        self.Bt_up = QtWidgets.QPushButton(self.widget)
        self.Bt_up.setObjectName("Bt_up")
        self.Bt_up.setMaximumWidth(100)
        self.Bt_up.setMinimumHeight(30)
        self.Bt_down = QtWidgets.QPushButton(self.widget)
        self.Bt_down.setObjectName("Bt_down")
        self.Bt_down.setMaximumWidth(100)
        self.Bt_down.setMinimumHeight(30)
        # Label 创建
        self.label_master = QtWidgets.QLabel(self.widget)
        self.label_master.setObjectName("label_master")
        self.label_master.setMaximumHeight(30)
        self.label_master.setAlignment(QtCore.Qt.AlignBottom)

        self.label_local = QtWidgets.QLabel(self.widget)
        self.label_local.setObjectName("label_local")
        self.label_local.setMaximumHeight(30)
        self.label_local.setAlignment(QtCore.Qt.AlignBottom)

        # treeView 创建
        self.treeWidget_master = QtWidgets.QTreeWidget(self.widget)
        self.treeWidget_master.setObjectName("treeWidget_master")
        self.treeWidget_master.header().hide()

        self.treeView_local = QtWidgets.QTreeView(self.widget)
        self.treeView_local.setObjectName("treeView_local")
        # spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_file.addWidget(self.label_master, 0, 0, 1, 1)
        self.gridLayout_file.addWidget(self.label_local, 0, 3, 1, 1)
        self.gridLayout_file.addWidget(self.treeWidget_master, 1, 0, 5, 2)
        self.gridLayout_file.addWidget(self.treeView_local, 1, 3, 5, 2)
        self.gridLayout_file.addWidget(self.Bt_down, 2, 2, 1, 1)
        self.gridLayout_file.addWidget(self.Bt_up, 3, 2, 1, 1)

        # self.gridLayout_file.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout_file.setSpacing(20)

    # 重载窗口大小函数
    def resizeEvent(self, QResizeEvent):
        QtWidgets.QWidget.resizeEvent(self, QResizeEvent)
        self.widget.setFixedSize(QSize(self.width()-20,self.height()-30))