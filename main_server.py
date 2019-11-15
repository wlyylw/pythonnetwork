import doc
import sys
from PyQt5 import QtWidgets
from server_ui import Ui_Form
from PyQt5.QtWidgets import *
import os
import net1
import threadServer




class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):

    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        # self.server = net1.server_operator()
        # self.server.tcp_operator()
        # self.conn = self.server.get_conn()
        # self.addr = self.server.get_addr()

        self.thread_server = threadServer.thread_server(1,"server1")
        self.thread_server.start()
        self.conn = self.thread_server.get_conn()
        self.addr = self.thread_server.get_addr()




        self.msg = ""  #得分



        self.start_test.clicked.connect(self.btn_start_test)
        self.end_test.clicked.connect(self.btn_end_test)
        self.see_grade.clicked.connect(self.btn_see_grade)
        self.select_topic.clicked.connect(self.btn_select_topic)


    def btn_select_topic(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "导入试题", self.cwd,"All Files (*);;Text Files (*.txt)")
        if fileName_choose == "":
            self.textEdit.setText("取消了选择")
            return
        else:
            self.textEdit.setText("导入完成")
            print(fileName_choose)
            self.list = doc.clissfy(fileName_choose)


    def btn_start_test(self):
        self.textEdit.setText("考试开始")
        # self.server.pre_start_test()
        self.thread_server.pre_start_test()

        #TODO：加一个线程收消息


    def btn_see_grade(self):
        addr = self.thread_server.get_addr()
        self.textEdit.setText("用户" +str(addr)+"得分"+self.msg )

    def btn_end_test(self):
        data = self.thread_server.get_conn().recv(1024)  # 收缓存为空，则阻塞
        self.msg = data.decode('utf-8')
        self.textEdit.setText("考试结束,可以查看成绩")
        pass
        #
        # if len(self.conn.recv(1024)) != 0:
        #     print("Not None")
        #     self.textEdit.setText("Not None")
        # else:
        #     pass
            #     self.server.server_close_conn()
        #     print("None")



        # data = self.conn.recv(1024)  # 收缓存为空，则阻塞
        # #
        # self.msg = data.decode('utf-8')
        # if self.msg != "":
        #     print('客户端发来的消息是', self.msg)
        #     print("考试结束")
        #     self.server.server_close_conn()
        # else:
        #     print("未交卷")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())

