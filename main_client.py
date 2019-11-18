import sys
from PyQt5 import QtWidgets
from client_ui import Ui_Form
import os
import re

import threadClient

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.btn_start_test.clicked.connect(self.on_start_test)
        self.btn_start_error.clicked.connect(self.on_see_error)
        self.flag = 0
        self.error_detail = 0
        self.score = 0
        self.thread_client = threadClient.thread_client(1, "client1")
        self.thread_client.start()





    def on_last_topic(self):
        if (self.current_page <= 0):
            pass
        else:
            self.current_page -= 1
            self.stackedWidget.setCurrentIndex(self.current_page)

    def on_next_topic(self):
        if (self.current_page >= 9):
            pass
        else:
            self.current_page += 1
            self.stackedWidget.setCurrentIndex(self.current_page)

    def on_start_test(self):
        if  self.flag == 0:
            self.flag+=1
            self.btn_last_topic.setVisible(True)
            self.btn_next_topic.setVisible(True)
            self.Topicend.setVisible(False)
            self.Topicend2.setVisible(False)
            self.Topicend3.setVisible(False)
            self.Topicend4.setVisible(False)
            self.btn_start_test.setText("提交答卷")

            self.list = self.thread_client.pre_start_test()

            self.current_page = 0
            self.classify_topic()
            self.stackedWidget.setCurrentIndex(self.current_page)
        elif self.flag == 1:        #提交答案
            self.flag += 1
            msg = self.get_sum()
            self.thread_client.send_mes(str(msg))

            self.Topicend.setVisible(True)
            self.Topicend2.setVisible(True)
            self.Topicend3.setVisible(True)
            self.Topicend4.setVisible(True)
            self.btn_next_topic.setVisible(False)
            self.btn_last_topic.setVisible(False)
            self.current_page = 11
            self.stackedWidget.setCurrentIndex(self.current_page)
            self.btn_start_test.setText("查看答题情况")
            self.get_sum()
        elif self.flag == 2 and (self.error_detail < len(self.error_list)):
            self.btn_start_error.setVisible(True)
            self.btn_start_test.setText("查看下一题")
            self.Topicend.setText("你答对了 " + str(self.right_num) + " 题,"
                                  + " 你的得分为 " + str(self.score) )
            self.error_num = len(self.error_list)
            self.error_detail+= 1
            self.current_page+= 1
            self.flag += 1
            self.stackedWidget.setCurrentIndex(self.current_page)
            self.retroction_situtation(self.error_detail)
        elif self.flag == 3 and (self.error_detail < self.error_num-1):
            self.error_detail+=1
            self.retroction_situtation(self.error_detail)

            self.flag+=1
        elif self.flag == 4 and (self.error_detail < self.error_num-1) :
            self.error_detail += 1
            self.retroction_situtation(self.error_detail)
            self.flag+=1
        elif self.flag == 5 and (self.error_detail < self.error_num-1):
            self.error_detail+=1
            self.retroction_situtation(self.error_detail)
            self.flag+=1
        elif self.flag == 6 and (self.error_detail < self.error_num-1):
            self.error_detail+=1
            self.retroction_situtation(self.error_detail)
            self.flag+=1
        elif self.flag == 7 and (self.error_detail < self.error_num-1) :
            self.error_detail+=1
            self.retroction_situtation(self.error_detail)

            self.flag+=1
        elif self.flag == 8 and (self.error_detail < self.error_num-1):
            self.error_detail += 1
            self.retroction_situtation(self.error_detail)
            self.flag+=1
        elif self.flag == 9 and (self.error_detail < self.error_num-1) :
            self.error_detail += 1
            self.retroction_situtation(self.error_detail)
            self.flag+=1
        elif self.flag == 10 and (self.error_detail < self.error_num-1):
            self.error_detail += 1
            self.retroction_situtation(self.error_detail)
            self.flag+=1
        elif self.flag == 11 and (self.error_detail < self.error_num-1):
            self.retroction_situtation(self.error_detail)
        else:
            self.retroction_situtation(self.error_detail)

    def classify_topic(self):
        pattern_A = re.compile('A.?(.*?)B')  # 去掉题目前面标号的正则
        pattern_B = re.compile('B.?(.*?)C')
        pattern_C = re.compile('C.?(.*?)D')
        pattern_D = re.compile('D.?(.*?)$')
        
        
        topic_list = self.list
        
        #0
        self.Topic0.setText("1、 " + topic_list[0].information)
        self.radioButton_0A.setText("A、 " + pattern_A.findall(topic_list[0].option)[0])
        self.radioButton_0B.setText("B、 " + pattern_B.findall(topic_list[0].option)[0])
        self.radioButton_0C.setText("C、 " + pattern_C.findall(topic_list[0].option)[0])
        self.radioButton_0D.setText("D、 " + pattern_D.findall(topic_list[0].option)[0])

        #1
        self.Topic1.setText("2、 "+topic_list[1].information)
        self.radioButton_1A.setText("A、 " + pattern_A.findall(topic_list[1].option)[0])
        self.radioButton_1B.setText("B、 " + pattern_B.findall(topic_list[1].option)[0])
        self.radioButton_1C.setText("C、 " + pattern_C.findall(topic_list[1].option)[0])
        self.radioButton_1D.setText("D、 " +pattern_D.findall(topic_list[1].option)[0])
        
        #2
        self.Topic2.setText("3、 "+topic_list[2].information)
        self.radioButton_2A.setText("A、 " + pattern_A.findall(topic_list[2].option)[0])
        self.radioButton_2B.setText("B、 " + pattern_B.findall(topic_list[2].option)[0])
        self.radioButton_2C.setText("C、 " + pattern_C.findall(topic_list[2].option)[0])
        self.radioButton_2D.setText("D、 " +pattern_D.findall(topic_list[2].option)[0])

        # 3
        self.Topic3.setText("4、 "+topic_list[3].information)
        self.radioButton_3A.setText("A、 " + pattern_A.findall(topic_list[3].option)[0])
        self.radioButton_3B.setText("B、 " + pattern_B.findall(topic_list[3].option)[0])
        self.radioButton_3C.setText("C、 " + pattern_C.findall(topic_list[3].option)[0])
        self.radioButton_3D.setText("D、 " +pattern_D.findall(topic_list[3].option)[0])

        # 4
        self.Topic4.setText("5、 "+topic_list[4].information)
        self.radioButton_4A.setText("A、 " + pattern_A.findall(topic_list[4].option)[0])
        self.radioButton_4B.setText("B、 " + pattern_B.findall(topic_list[4].option)[0])
        self.radioButton_4C.setText("C、 " + pattern_C.findall(topic_list[4].option)[0])
        self.radioButton_4D.setText("D、 " +pattern_D.findall(topic_list[4].option)[0])

        # 5
        self.Topic5.setText("6、 "+topic_list[5].information)
        self.radioButton_5A.setText("A、 " + pattern_A.findall(topic_list[5].option)[0])
        self.radioButton_5B.setText("B、 " + pattern_B.findall(topic_list[5].option)[0])
        self.radioButton_5C.setText("C、 " + pattern_C.findall(topic_list[5].option)[0])
        self.radioButton_5D.setText("D、 " +pattern_D.findall(topic_list[5].option)[0])

        # 6
        self.Topic6.setText("7、 "+topic_list[6].information)
        self.radioButton_6A.setText("A、 " + pattern_A.findall(topic_list[6].option)[0])
        self.radioButton_6B.setText("B、 " + pattern_B.findall(topic_list[6].option)[0])
        self.radioButton_6C.setText("C、 " + pattern_C.findall(topic_list[6].option)[0])
        self.radioButton_6D.setText("D、 " +pattern_D.findall(topic_list[6].option)[0])

        # 7
        self.Topic7.setText("8、 "+topic_list[7].information)
        self.radioButton_7A.setText("A、 " + pattern_A.findall(topic_list[7].option)[0])
        self.radioButton_7B.setText("B、 " + pattern_B.findall(topic_list[7].option)[0])
        self.radioButton_7C.setText("C、 " + pattern_C.findall(topic_list[7].option)[0])
        self.radioButton_7D.setText("D、 " +pattern_D.findall(topic_list[7].option)[0])

        # 8
        self.Topic8.setText("9、 "+topic_list[8].information)
        self.radioButton_8A.setText("A、 " + pattern_A.findall(topic_list[8].option)[0])
        self.radioButton_8B.setText("B、 " + pattern_B.findall(topic_list[8].option)[0])
        self.radioButton_8C.setText("C、 " + pattern_C.findall(topic_list[8].option)[0])
        self.radioButton_8D.setText("D、 " +pattern_D.findall(topic_list[8].option)[0])

        # 9
        self.Topic9.setText("10、 "+topic_list[9].information)
        self.radioButton_9A.setText("A、 " + pattern_A.findall(topic_list[9].option)[0])
        self.radioButton_9B.setText("B、 " + pattern_B.findall(topic_list[9].option)[0])
        self.radioButton_9C.setText("C、 " + pattern_C.findall(topic_list[9].option)[0])
        self.radioButton_9D.setText("D、 " +pattern_D.findall(topic_list[9].option)[0])

    def get_sum(self):
        answer_list = self.get_checked()
        self.score = 0
        self.right_num =0
        self.error_list_answer  = [] #错题集自选答案
        self.error_list = []         #错的序号

        for i in range(0, 10):
            if answer_list[i] == self.list[i].answer:
                self.score += 10
                self.right_num += 1
            else:
                self.error_list.append(i)
                self.error_list_answer.append(answer_list[i])
        # print(self.error_list)
        # print(self.error_list_answer)
        print("总分： " + str(self.score))
        print("答对题数: "+ str(self.right_num))
        return self.score
    def on_see_error(self):
        if self.error_detail == 0:
            self.retroction_situtation(self.error_detail)
        else:
            self.error_detail -= 1
            self.flag-=1
            self.retroction_situtation(self.error_detail)


    def get_checked(self):
        #0
        check = []
        if self.radioButton_0A.isChecked():
            check0 = 'A'
        elif self.radioButton_0B.isChecked():
            check0 = 'B'
        elif self.radioButton_0C.isChecked():
            check0 = 'C'
        elif self.radioButton_0D.isChecked():
            check0 = 'D'
        else:
            check0 = 'N'
        #1
        if self.radioButton_1A.isChecked():
            check1 = 'A'
        elif self.radioButton_1B.isChecked():
            check1 = 'B'
        elif self.radioButton_1C.isChecked():
            check1 = 'C'
        elif self.radioButton_1D.isChecked():
            check1 = 'D'
        else:
            check1 = 'N'
        #2
        if self.radioButton_2A.isChecked():
            check2 = 'A'
        elif self.radioButton_2B.isChecked():
            check2 = 'B'
        elif self.radioButton_2C.isChecked():
            check2 = 'C'
        elif self.radioButton_2D.isChecked():
            check2 = 'D'
        else:
            check2 = 'N'
        #3
        if self.radioButton_3A.isChecked():
            check3 = 'A'
        elif self.radioButton_3B.isChecked():
            check3 = 'B'
        elif self.radioButton_3C.isChecked():
            check3 = 'C'
        elif self.radioButton_3D.isChecked():
            check3 = 'D'
        else:
            check3 = 'N'
        #4
        if self.radioButton_4A.isChecked():
            check4 = 'A'
        elif self.radioButton_4B.isChecked():
            check4 = 'B'
        elif self.radioButton_4C.isChecked():
            check4 = 'C'
        elif self.radioButton_4D.isChecked():
            check4 = 'D'
        else:
            check4 = 'N'
        #5
        if self.radioButton_5A.isChecked():
            check5 = 'A'
        elif self.radioButton_5B.isChecked():
            check5 = 'B'
        elif self.radioButton_5C.isChecked():
            check5 = 'C'
        elif self.radioButton_5D.isChecked():
            check5 = 'D'
        else:
            check5 = 'N'
        #6
        if self.radioButton_6A.isChecked():
            check6 = 'A'
        elif self.radioButton_6B.isChecked():
            check6 = 'B'
        elif self.radioButton_6C.isChecked():
            check6 = 'C'
        elif self.radioButton_6D.isChecked():
            check6 = 'D'
        else:
            check6 = 'N'
        #7
        if self.radioButton_7A.isChecked():
            check7 = 'A'
        elif self.radioButton_7B.isChecked():
            check7 = 'B'
        elif self.radioButton_7C.isChecked():
            check7 = 'C'
        elif self.radioButton_7D.isChecked():
            check7 = 'D'
        else:
            check7 = 'N'
        #8
        if self.radioButton_8A.isChecked():
            check8 = 'A'
        elif self.radioButton_8B.isChecked():
            check8 = 'B'
        elif self.radioButton_8C.isChecked():
            check8 = 'C'
        elif self.radioButton_8D.isChecked():
            check8 = 'D'
        else:
            check8 = 'N'
        #9
        if self.radioButton_9A.isChecked():
            check9 = 'A'
        elif self.radioButton_9B.isChecked():
            check9 = 'B'
        elif self.radioButton_9B.isChecked():
            check9 = 'C'
        elif self.radioButton_9D.isChecked():
            check9 = 'D'
        else:
            check9 = 'N'
        check.append(check0)
        check.append(check1)
        check.append(check2)
        check.append(check3)
        check.append(check4)
        check.append(check5)
        check.append(check6)
        check.append(check7)
        check.append(check8)
        check.append(check9)
        return check

    #上端调用 生成具体错题情况
    def retroction_situtation(self,num):
        self.Topicend2.setText("error" + str(num) + ":  " + self.list[self.error_list[num]].information)
        self.Topicend3.setText(self.list[self.error_list[num]].option)
        self.Topicend4.setText(
        "the right option is  "  +  self.list[self.error_list[num]].answer +
        "  you choose " + self.error_list_answer[num]
        )
        pass
    #写哪些题错了



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())