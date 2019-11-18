from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import tkinter
import time
import threading

class Ui_Form(object):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.current_page = 0  # 当前页数

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 655)

        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 30, 1041, 461))
        self.stackedWidget.setObjectName("stackedWidget")

        ###########################

        # page0
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.Topic0 = QtWidgets.QLabel(self.page0)
        self.Topic0.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic0.setObjectName("Topic0")

        self.radioButton_0A = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_0A.setObjectName("radioButton_0A")
        self.radioButton_0B = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_0B.setObjectName("radioButton_0B")
        self.radioButton_0C = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_0C.setObjectName("radioButton_0C")
        self.radioButton_0D = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_0D.setObjectName("radioButton_0D")
        self.stackedWidget.addWidget(self.page0)

        # page1
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.Topic1 = QtWidgets.QLabel(self.page1)
        self.Topic1.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic1.setObjectName("Topic1")

        self.radioButton_1A = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_1A.setObjectName("radioButton_1A")
        self.radioButton_1B = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_1B.setObjectName("radioButton_1B")
        self.radioButton_1C = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_1C.setObjectName("radioButton_1C")
        self.radioButton_1D = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_1D.setObjectName("radioButton_1D")
        self.stackedWidget.addWidget(self.page1)

        # page2
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.Topic2 = QtWidgets.QLabel(self.page2)
        self.Topic2.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic2.setObjectName("Topic2")
        self.radioButton_2A = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_2A.setObjectName("radioButton_2A")
        self.radioButton_2B = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_2B.setObjectName("radioButton_2B")
        self.radioButton_2C = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_2C.setObjectName("radioButton_2C")
        self.radioButton_2D = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_2D.setObjectName("radioButton_2D")
        self.stackedWidget.addWidget(self.page2)

        # page3
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.Topic3 = QtWidgets.QLabel(self.page3)
        self.Topic3.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic3.setObjectName("Topic3")
        self.radioButton_3A = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_3A.setObjectName("radioButton_3A")
        self.radioButton_3B = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_3B.setObjectName("radioButton_3B")
        self.radioButton_3C = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_3C.setObjectName("radioButton_3C")
        self.radioButton_3D = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_3D.setObjectName("radioButton_3D")
        self.stackedWidget.addWidget(self.page3)

        # page4
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.Topic4 = QtWidgets.QLabel(self.page4)
        self.Topic4.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic4.setObjectName("Topic4")
        self.radioButton_4A = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_4A.setObjectName("radioButton_4A")
        self.radioButton_4B = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_4B.setObjectName("radioButton_4B")
        self.radioButton_4C = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_4C.setObjectName("radioButton_4C")
        self.radioButton_4D = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_4D.setObjectName("radioButton_4D")
        self.stackedWidget.addWidget(self.page4)

        # page5
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.Topic5 = QtWidgets.QLabel(self.page5)
        self.Topic5.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic5.setObjectName("Topic5")
        self.radioButton_5A = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_5A.setObjectName("radioButton_5A")
        self.radioButton_5B = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_5B.setObjectName("radioButton_5B")
        self.radioButton_5C = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_5C.setObjectName("radioButton_5C")
        self.radioButton_5D = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_5D.setObjectName("radioButton_5D")
        self.stackedWidget.addWidget(self.page5)

        # page6
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.Topic6 = QtWidgets.QLabel(self.page6)
        self.Topic6.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic6.setObjectName("Topic6")
        self.radioButton_6A = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_6A.setObjectName("radioButton_6A")
        self.radioButton_6B = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_6B.setObjectName("radioButton_6B")
        self.radioButton_6C = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_6C.setObjectName("radioButton_6C")
        self.radioButton_6D = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_6D.setObjectName("radioButton_6D")
        self.stackedWidget.addWidget(self.page6)

        # page7
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName("page7")
        self.Topic7 = QtWidgets.QLabel(self.page7)
        self.Topic7.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic7.setObjectName("Topic7")
        self.radioButton_7A = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_7A.setObjectName("radioButton_7A")
        self.radioButton_7B = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_7B.setObjectName("radioButton_7B")
        self.radioButton_7C = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_7C.setObjectName("radioButton_7C")
        self.radioButton_7D = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_7D.setObjectName("radioButton_7D")
        self.stackedWidget.addWidget(self.page7)

        # page8
        self.page8 = QtWidgets.QWidget()
        self.page8.setObjectName("page8")
        self.Topic8 = QtWidgets.QLabel(self.page8)
        self.Topic8.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic8.setObjectName("Topic8")
        self.radioButton_8A = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_8A.setObjectName("radioButton_8A")
        self.radioButton_8B = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_8B.setObjectName("radioButton_8B")
        self.radioButton_8C = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_8C.setObjectName("radioButton_8C")
        self.radioButton_8D = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_8D.setObjectName("radioButton_8D")
        self.stackedWidget.addWidget(self.page8)

        # page9
        self.page9 = QtWidgets.QWidget()
        self.page9.setObjectName("page9")
        self.Topic9 = QtWidgets.QLabel(self.page9)
        self.Topic9.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic9.setObjectName("Topic9")
        self.radioButton_9A = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9A.setGeometry(QtCore.QRect(130, 150, 250, 19))
        self.radioButton_9A.setObjectName("radioButton_9A")
        self.radioButton_9B = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9B.setGeometry(QtCore.QRect(570, 150, 250, 19))
        self.radioButton_9B.setObjectName("radioButton_9B")
        self.radioButton_9C = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9C.setGeometry(QtCore.QRect(130, 230, 250, 19))
        self.radioButton_9C.setObjectName("radioButton_9C")
        self.radioButton_9D = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9D.setGeometry(QtCore.QRect(570, 230, 250, 20))
        self.radioButton_9D.setObjectName("radioButton_9D")
        self.stackedWidget.addWidget(self.page9)

        # ZZZZZZZZZZZZ
        # pagestart
        self.pagestart = QtWidgets.QWidget()
        self.pagestart.setObjectName("pagestart")
        self.Topic = QtWidgets.QLabel(self.pagestart)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topicstart")
        self.stackedWidget.addWidget(self.pagestart)

        self.btn_start_test = QtWidgets.QPushButton(Form)
        self.btn_start_test.setGeometry(QtCore.QRect(430, 580, 131, 41))  # TODO：位置
        self.btn_start_test.setObjectName("btn_start_test")

        self.btn_start_error = QtWidgets.QPushButton(Form)
        self.btn_start_error.setGeometry(QtCore.QRect(430, 530, 131, 41))  # TODO：位置
        self.btn_start_error.setObjectName("btn_start_error")



        # self.btn_start_test.clicked.connect(self.on_start_test)

        # ZZZZZZZZZZZZ
        # pageend
        self.pageend = QtWidgets.QLabel(Form)
        self.pageend.setObjectName("pageend")
        self.Topicend = QtWidgets.QLabel(Form)
        self.Topicend.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topicend.setObjectName("Topicend")
        self.Topicend2 = QtWidgets.QLabel(Form)
        self.Topicend2.setGeometry(QtCore.QRect(30, 60, 991, 111))
        self.Topicend2.setObjectName("Topicend2")

        self.Topicend3 = QtWidgets.QLabel(Form)
        self.Topicend3.setGeometry(QtCore.QRect(30, 105, 991, 111))
        self.Topicend3.setObjectName("Topicend3")

        self.Topicend4 = QtWidgets.QLabel(Form)
        self.Topicend4.setGeometry(QtCore.QRect(30, 150, 991, 111))
        self.Topicend4.setObjectName("Topicend4")

        self.stackedWidget.addWidget(self.pageend)  # 430, 280, 131, 41

        # ZZZZZZZZZZZZ
        # pageerror1
        self.pageerror1 = QtWidgets.QWidget()
        self.pageerror1.setObjectName("pageerror1")
        self.Topicerror = QtWidgets.QLabel(self.pageerror1)
        self.Topicerror.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topicerror.setObjectName("Topicerror")
        self.Topicerror2 = QtWidgets.QLabel(self.pageerror1)
        self.Topicerror2.setGeometry(QtCore.QRect(30, 60, 991, 111))
        self.Topicerror2.setObjectName("Topicerror2")

        self.Topicerror3 = QtWidgets.QLabel(self.pageerror1)
        self.Topicerror3.setGeometry(QtCore.QRect(30, 105, 991, 111))
        self.Topicerror3.setObjectName("Topicerror3")

        self.Topicerror4 = QtWidgets.QLabel(self.pageerror1)
        self.Topicerror4.setGeometry(QtCore.QRect(30, 150, 991, 111))
        self.Topicerror4.setObjectName("Topicerror4")

        self.stackedWidget.addWidget(self.pageerror1)  #

        # ZZZZZZZZZZZZ
        # error page
        # pageerror0
        self.pageerror0 = QtWidgets.QWidget()
        self.pageerror0.setObjectName("pageerror0")
        self.stackedWidget.addWidget(self.pageerror0)  #


        #未在规定时间完成  page 2222
        self.pageundo = QtWidgets.QWidget()
        self.pageundo.setObjectName("pageundo")
        self.stackedWidget.addWidget(self.pageundo)  #
        self.undo = QtWidgets.QLabel(self.pageundo)
        self.undo.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.undo.setObjectName("undo")
        self.undo.setText("未在规定时间内完成")


        #############################
        self.btn_last_topic = QtWidgets.QPushButton(Form)
        self.btn_last_topic.setGeometry(QtCore.QRect(40, 580, 131, 41))
        self.btn_last_topic.setObjectName("btn_last_topic")

        self.btn_next_topic = QtWidgets.QPushButton(Form)
        self.btn_next_topic.setGeometry(QtCore.QRect(910, 580, 131, 41))
        self.btn_next_topic.setObjectName("btn_next_topic")
        
        
        self.tktime = QtWidgets.QLabel(Form)
        self.tktime.setGeometry(QtCore.QRect(430, 10, 200, 41))
        self.tktime.setObjectName("tktime")

        self.btn_last_topic.clicked.connect(self.on_last_topic)
        self.btn_next_topic.clicked.connect(self.on_next_topic)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "在线考试系统"))

        self.btn_next_topic.setText(_translate("Form", "下一页"))
        self.btn_last_topic.setText(_translate("Form", "上一页"))
        self.btn_start_test.setText(_translate("Form", "开始考试"))
        self.btn_start_error.setText(_translate("Form", "查看上一题"))
        self.btn_start_error.setVisible(False)
        self.btn_last_topic.setVisible(False)
        self.btn_next_topic.setVisible(False)
        self.stackedWidget.setCurrentIndex(10)


