import threading
from socket import *
import doc
import random
import json


def DeSerializ(t):
    return doc.Topic(
         t["information"],
         t["answer"],
         t["option"]
    )

ip_port = ('127.0.0.1', 8080)
back_log = 40
buffer_size = 1024

class thread_client(threading.Thread):
    def __init__(self, threadID , name):
        threading.Thread.__init__(self)
        self.name = name
        self.threadID = threadID
        self.name = name
        self.tcp_operator()

    def tcp_operator(self):
        self.tcp_client = socket(AF_INET, SOCK_STREAM)
        self.tcp_client.connect(ip_port)

    def pre_start_test(self):
            list = []
            for i in range(0,10):
                if(i==9):
                    msg = "end"
                else:
                    msg="start"
                self.tcp_client.send(msg.encode('utf-8'))
                # print('客户端已经发送消息')
                data = self.tcp_client.recv(buffer_size)  #收缓存为空则阻塞
                data=data.decode('utf-8')
                data = json.loads(data,object_hook=DeSerializ)
                topic = doc.Topic(data.information,data.answer,data.option)
                list.append(topic)
            return list

    def tcp_operator_close(self):
        self.tcp_client.close()

    def send_mes(self,msg):
        self.tcp_client.send(msg.encode('utf-8'))

    def run(self):
        currentTreadname = threading.currentThread()
        print("running in", currentTreadname)