# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(849, 609)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(False)
        Form.setFont(font)
        self.select_topic = QtWidgets.QPushButton(Form)
        self.select_topic.setGeometry(QtCore.QRect(90, 40, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.select_topic.setFont(font)
        self.select_topic.setAutoRepeatDelay(300)
        self.select_topic.setObjectName("slect_topic")
        self.end_test = QtWidgets.QPushButton(Form)
        self.end_test.setGeometry(QtCore.QRect(470, 200, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.end_test.setFont(font)
        self.end_test.setAutoRepeatDelay(300)
        self.end_test.setObjectName("end_test")
        self.see_grade = QtWidgets.QPushButton(Form)
        self.see_grade.setGeometry(QtCore.QRect(90, 200, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.see_grade.setFont(font)
        self.see_grade.setAutoRepeatDelay(300)
        self.see_grade.setObjectName("see_grade")
        self.start_test = QtWidgets.QPushButton(Form)
        self.start_test.setGeometry(QtCore.QRect(470, 40, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.start_test.setFont(font)
        self.start_test.setAutoRepeatDelay(300)
        self.start_test.setObjectName("start_test")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(130, 390, 551, 87))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select_topic.setText(_translate("Form", "选择题库"))
        self.end_test.setText(_translate("Form", "结束考试"))
        self.see_grade.setText(_translate("Form", "查看成绩"))
        self.start_test.setText(_translate("Form", "开始考试"))

