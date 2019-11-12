from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(849, 524)
        self.client_start_test = QtWidgets.QPushButton(Form)
        self.client_start_test.setGeometry(QtCore.QRect(270, 130, 311, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.client_start_test.setFont(font)
        self.client_start_test.setObjectName("cline_start_test")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "在线考试系统"))
        self.client_start_test.setText(_translate("Form", "开始考试"))


