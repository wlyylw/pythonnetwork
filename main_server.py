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
        self.msg = None
        self.score =None
        self.text = ""
        self.StartTest = 0
        self.EndTest = 0

        self.serverthread = st.ServerThread()


    def btn_select_topic(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "导入试题", self.cwd,"All Files (*);;Text Files (*.txt)")
        if fileName_choose == "":
            return
        else:
            self.text += "导入完成\n"
            self.textEdit.setText(self.text)
            self.serverthread.setPath(fileName_choose)
            print(fileName_choose)



    def btn_start_test(self):
        serverthread = self.serverthread
        if serverthread.path != None:
            if self.isFirstStartThread == 0 :
                self.isFirstStartThread = 1
                serverthread.start()
                self.text = ""
                self.text += "考试开始\n"
                self.textEdit.setText(self.text)
                self.StartTest = 1

            else:
                pass
        else:
            self.textEdit.setText("请先选择考题\n")
            pass





    def btn_see_grade(self):
        if self.EndTest ==1:
            self.textEdit.setText(self.text)
            print("线程关闭")
        else:
            pass

    def btn_end_test(self):
        if self.StartTest == 1:
            score = ""
            score_list = self.serverthread.score_list
            for i in range(0, len(score_list)):
                score += "用户" + str(score_list[i]) + "\n"
            self.text += "考试已结束"
            self.textEdit.setText(self.text)
            self.text = self.text + "\n" + score
            self.EndTest = 1
            self.serverthread.close_tcp()
        else:
            pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())

