import doc
import sys
from PyQt5 import QtWidgets
from server_ui import Ui_Form
from PyQt5.QtWidgets import *
import os

import st




class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.isFirstStartThread = 0
        self.start_test.clicked.connect(self.btn_start_test)
        self.end_test.clicked.connect(self.btn_end_test)
        self.see_grade.clicked.connect(self.btn_see_grade)
        self.select_topic.clicked.connect(self.btn_select_topic)


        self.serverthread = st.ServerThread()


    def btn_select_topic(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "导入试题", self.cwd,"All Files (*);;Text Files (*.txt)")
        if fileName_choose == "":
            self.textEdit.setText("取消了选择")
            return
        else:
            self.textEdit.setText("导入完成")
            print(fileName_choose)



    def btn_start_test(self):
        serverthread = self.serverthread
        if self.isFirstStartThread == 0 :
            self.isFirstStartThread = 1
            serverthread.start()
        else:
            pass



    def btn_see_grade(self):
        pass

    def btn_end_test(self):
        pass




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())

