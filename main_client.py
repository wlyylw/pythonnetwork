import doc
import sys
from PyQt5 import QtWidgets
from client_ui import Ui_Form
from PyQt5.QtWidgets import *
import os
import re
import net2

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.btn_start_test.clicked.connect(self.on_start_test)

    def on_start_test(self):
        client = net2.client_operator()
        print("客户端开始运行")
        client.tcp_operator()
        self.list = client.pre_start_test()
        self.btn_last_topic.setVisible(True)
        self.btn_next_topic.setVisible(True)
        print(self.list[0].option)
        self.current_page = 0
        self.classify_topic()
        self.stackedWidget.setCurrentIndex(self.current_page)

    def classify_topic(self):
        pattern_A = re.compile('A.?(.*?)B')  # 去掉题目前面标号的正则
        pattern_B = re.compile('B.?(.*?)C')
        pattern_C = re.compile('C.?(.*?)D')
        pattern_D = re.compile('D.?(.*?)$')
        
        
        topic_list = self.list
        
        #0
        self.Topic0.setText(topic_list[0].information)
        self.radioButton_0A.setText(pattern_A.findall(topic_list[0].option)[0])
        self.radioButton_0B.setText(pattern_B.findall(topic_list[0].option)[0])
        self.radioButton_0C.setText(pattern_C.findall(topic_list[0].option)[0])
        self.radioButton_0D.setText(pattern_D.findall(topic_list[0].option)[0])

        #1
        self.Topic1.setText(topic_list[1].information)
        self.radioButton_1A.setText(pattern_A.findall(topic_list[1].option)[0])
        self.radioButton_1B.setText(pattern_B.findall(topic_list[1].option)[0])
        self.radioButton_1C.setText(pattern_C.findall(topic_list[1].option)[0])
        self.radioButton_1D.setText(pattern_D.findall(topic_list[1].option)[0])
        
        #2
        self.Topic2.setText(topic_list[2].information)
        self.radioButton_2A.setText(pattern_A.findall(topic_list[2].option)[0])
        self.radioButton_2B.setText(pattern_B.findall(topic_list[2].option)[0])
        self.radioButton_2C.setText(pattern_C.findall(topic_list[2].option)[0])
        self.radioButton_2D.setText(pattern_D.findall(topic_list[2].option)[0])

        # 3
        self.Topic3.setText(topic_list[3].information)
        self.radioButton_3A.setText(pattern_A.findall(topic_list[3].option)[0])
        self.radioButton_3B.setText(pattern_B.findall(topic_list[3].option)[0])
        self.radioButton_3C.setText(pattern_C.findall(topic_list[3].option)[0])
        self.radioButton_3D.setText(pattern_D.findall(topic_list[3].option)[0])

        # 4
        self.Topic4.setText(topic_list[4].information)
        self.radioButton_4A.setText(pattern_A.findall(topic_list[4].option)[0])
        self.radioButton_4B.setText(pattern_B.findall(topic_list[4].option)[0])
        self.radioButton_4C.setText(pattern_C.findall(topic_list[4].option)[0])
        self.radioButton_4D.setText(pattern_D.findall(topic_list[4].option)[0])

        # 5
        self.Topic5.setText(topic_list[5].information)
        self.radioButton_5A.setText(pattern_A.findall(topic_list[5].option)[0])
        self.radioButton_5B.setText(pattern_B.findall(topic_list[5].option)[0])
        self.radioButton_5C.setText(pattern_C.findall(topic_list[5].option)[0])
        self.radioButton_5D.setText(pattern_D.findall(topic_list[5].option)[0])

        # 6
        self.Topic6.setText(topic_list[6].information)
        self.radioButton_6A.setText(pattern_A.findall(topic_list[6].option)[0])
        self.radioButton_6B.setText(pattern_B.findall(topic_list[6].option)[0])
        self.radioButton_6C.setText(pattern_C.findall(topic_list[6].option)[0])
        self.radioButton_6D.setText(pattern_D.findall(topic_list[6].option)[0])

        # 7
        self.Topic7.setText(topic_list[7].information)
        self.radioButton_7A.setText(pattern_A.findall(topic_list[7].option)[0])
        self.radioButton_7B.setText(pattern_B.findall(topic_list[7].option)[0])
        self.radioButton_7C.setText(pattern_C.findall(topic_list[7].option)[0])
        self.radioButton_7D.setText(pattern_D.findall(topic_list[7].option)[0])

        # 8
        self.Topic8.setText(topic_list[8].information)
        self.radioButton_8A.setText(pattern_A.findall(topic_list[8].option)[0])
        self.radioButton_8B.setText(pattern_B.findall(topic_list[8].option)[0])
        self.radioButton_8C.setText(pattern_C.findall(topic_list[8].option)[0])
        self.radioButton_8D.setText(pattern_D.findall(topic_list[8].option)[0])

        # 9
        self.Topic9.setText(topic_list[9].information)
        self.radioButton_9A.setText(pattern_A.findall(topic_list[9].option)[0])
        self.radioButton_9B.setText(pattern_B.findall(topic_list[9].option)[0])
        self.radioButton_9C.setText(pattern_C.findall(topic_list[9].option)[0])
        self.radioButton_9D.setText(pattern_D.findall(topic_list[9].option)[0])
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())