# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qstack.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Ui_Form(QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 655)
        



        #page 1
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 30, 1041, 461))
        self.stackedWidget.setObjectName("stackedWidget")

        ###########################



        #page0
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.Topic = QtWidgets.QLabel(self.page0)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic0")
        self.radioButton_0A = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_0A.setObjectName("radioButton_0A")
        self.radioButton_0B = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_0B.setObjectName("radioButton_0B")
        self.radioButton_0C = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_0C.setObjectName("radioButton_0C")
        self.radioButton_0D = QtWidgets.QRadioButton(self.page0)
        self.radioButton_0D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_0D.setObjectName("radioButton_0D")
        self.stackedWidget.addWidget(self.page0)


        #page1
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.Topic = QtWidgets.QLabel(self.page1)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic1")
        self.radioButton_1A = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_1A.setObjectName("radioButton_1A")
        self.radioButton_1B = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_1B.setObjectName("radioButton_1B")
        self.radioButton_1C = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_1C.setObjectName("radioButton_1C")
        self.radioButton_1D = QtWidgets.QRadioButton(self.page1)
        self.radioButton_1D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_1D.setObjectName("radioButton_1D")
        self.stackedWidget.addWidget(self.page1)

        #page2
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.Topic = QtWidgets.QLabel(self.page2)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic2")
        self.radioButton_2A = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_2A.setObjectName("radioButton_2A")
        self.radioButton_2B = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_2B.setObjectName("radioButton_2B")
        self.radioButton_2C = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_2C.setObjectName("radioButton_2C")
        self.radioButton_2D = QtWidgets.QRadioButton(self.page2)
        self.radioButton_2D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_2D.setObjectName("radioButton_2D")
        self.stackedWidget.addWidget(self.page2)
        
        
        #page3
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.Topic = QtWidgets.QLabel(self.page3)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic3")
        self.radioButton_3A = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_3A.setObjectName("radioButton_3A")
        self.radioButton_3B = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_3B.setObjectName("radioButton_3B")
        self.radioButton_3C = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_3C.setObjectName("radioButton_3C")
        self.radioButton_3D = QtWidgets.QRadioButton(self.page3)
        self.radioButton_3D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_3D.setObjectName("radioButton_3D")
        self.stackedWidget.addWidget(self.page3)

        #page4
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.Topic = QtWidgets.QLabel(self.page4)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic4")
        self.radioButton_4A = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_4A.setObjectName("radioButton_4A")
        self.radioButton_4B = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_4B.setObjectName("radioButton_4B")
        self.radioButton_4C = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_4C.setObjectName("radioButton_4C")
        self.radioButton_4D = QtWidgets.QRadioButton(self.page4)
        self.radioButton_4D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_4D.setObjectName("radioButton_4D")
        self.stackedWidget.addWidget(self.page4)
        
        #page5
        self.page5 = QtWidgets.QWidget()
        self.page5.setObjectName("page5")
        self.Topic = QtWidgets.QLabel(self.page5)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic5")
        self.radioButton_5A = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_5A.setObjectName("radioButton_5A")
        self.radioButton_5B = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_5B.setObjectName("radioButton_5B")
        self.radioButton_5C = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_5C.setObjectName("radioButton_5C")
        self.radioButton_5D = QtWidgets.QRadioButton(self.page5)
        self.radioButton_5D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_5D.setObjectName("radioButton_5D")
        self.stackedWidget.addWidget(self.page5)
        
        #page6
        self.page6 = QtWidgets.QWidget()
        self.page6.setObjectName("page6")
        self.Topic = QtWidgets.QLabel(self.page6)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic6")
        self.radioButton_6A = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_6A.setObjectName("radioButton_6A")
        self.radioButton_6B = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_6B.setObjectName("radioButton_6B")
        self.radioButton_6C = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_6C.setObjectName("radioButton_6C")
        self.radioButton_6D = QtWidgets.QRadioButton(self.page6)
        self.radioButton_6D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_6D.setObjectName("radioButton_6D")
        self.stackedWidget.addWidget(self.page6)
        
        
        #page7
        self.page7 = QtWidgets.QWidget()
        self.page7.setObjectName("page7")
        self.Topic = QtWidgets.QLabel(self.page7)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic7")
        self.radioButton_7A = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_7A.setObjectName("radioButton_7A")
        self.radioButton_7B = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_7B.setObjectName("radioButton_7B")
        self.radioButton_7C = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_7C.setObjectName("radioButton_7C")
        self.radioButton_7D = QtWidgets.QRadioButton(self.page7)
        self.radioButton_7D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_7D.setObjectName("radioButton_7D")
        self.stackedWidget.addWidget(self.page7)
        
        
        #page8
        self.page8 = QtWidgets.QWidget()
        self.page8.setObjectName("page8")
        self.Topic = QtWidgets.QLabel(self.page8)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic8")
        self.radioButton_8A = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_8A.setObjectName("radioButton_8A")
        self.radioButton_8B = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_8B.setObjectName("radioButton_8B")
        self.radioButton_8C = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_8C.setObjectName("radioButton_8C")
        self.radioButton_8D = QtWidgets.QRadioButton(self.page8)
        self.radioButton_8D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_8D.setObjectName("radioButton_8D")
        self.stackedWidget.addWidget(self.page8)
        
        
        #page9
        self.page9 = QtWidgets.QWidget()
        self.page9.setObjectName("page9")
        self.Topic = QtWidgets.QLabel(self.page9)
        self.Topic.setGeometry(QtCore.QRect(30, 15, 991, 111))
        self.Topic.setObjectName("Topic9")
        self.radioButton_9A = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9A.setGeometry(QtCore.QRect(130, 150, 115, 19))
        self.radioButton_9A.setObjectName("radioButton_9A")
        self.radioButton_9B = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9B.setGeometry(QtCore.QRect(570, 150, 115, 19))
        self.radioButton_9B.setObjectName("radioButton_9B")
        self.radioButton_9C = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9C.setGeometry(QtCore.QRect(130, 230, 115, 19))
        self.radioButton_9C.setObjectName("radioButton_9C")
        self.radioButton_9D = QtWidgets.QRadioButton(self.page9)
        self.radioButton_9D.setGeometry(QtCore.QRect(570, 230, 111, 20))
        self.radioButton_9D.setObjectName("radioButton_9D")
        self.stackedWidget.addWidget(self.page9)
        

        
        
        
        #############################
        self.btn_last_topic = QtWidgets.QPushButton(Form)
        self.btn_last_topic.setGeometry(QtCore.QRect(910, 580, 131, 41))
        self.btn_last_topic.setObjectName("btn_last_topic")
        self.btn_next_topic = QtWidgets.QPushButton(Form)
        self.btn_next_topic.setGeometry(QtCore.QRect(40, 580, 131, 41))
        self.btn_next_topic.setObjectName("btn_next_topic")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "在线考试系统"))
        self.Topic.setText(_translate("Form", "题目"))
        self.radioButton_1A.setText(_translate("Form", "A 选项"))
        self.radioButton_1B.setText(_translate("Form", "B 选项"))
        self.radioButton_1C.setText(_translate("Form", "C 选项"))
        self.radioButton_1D.setText(_translate("Form", "D 选项"))
        self.btn_last_topic.setText(_translate("Form", "下一页"))
        self.btn_next_topic.setText(_translate("Form", "上一页"))








if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = Ui_Form()
    the_mainwindow.show()
    sys.exit(app.exec_())