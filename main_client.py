import doc
import sys
from PyQt5 import QtWidgets
from client_ui import Ui_Form
from PyQt5.QtWidgets import *
import os
import net2

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.client_start_test.clicked.connect(self.btn_client_start_test)

    def btn_client_start_test(self):
        client = net2.client_operator()
        print("客户端开始运行")
        client.tcp_operator()
        client.pre_start_test()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())