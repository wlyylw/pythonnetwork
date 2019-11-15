from socket import *
import doc
import json
import random
import threading


def Serializ(Topic):

    return {
        "answer": Topic.answer,
        "option": Topic.option,
        "information": Topic.information
    }


list = doc.clissfy("E:\\Desktop\\kstk.docx")    #获取已经处理好的word文档中的信息

MAX_TOPIC = len(list)
random_list = random.sample(range(0,MAX_TOPIC), 10)

class server_operator():

    def __init__(self):
        self.number = 0

    def tcp_operator(self):
        tcp_server = socket(AF_INET, SOCK_STREAM)
        ip_port = ('127.0.0.1', 8080)
        tcp_server.bind(ip_port)
        tcp_server.listen(10)
        conn,addr = tcp_server.accept()  # 服务器阻塞
        self.conn = conn
        self.addr = addr



    def pre_start_test(self):
        while True:
            data = self.conn.recv(1024)  # 收缓存为空，则阻塞
            msg = data.decode('utf-8')
            print('客户端发来的消息是', msg)
            topic = list[random_list[self.number]]  # 随机10题
            topic = json.dumps(topic, default=Serializ)
            self.conn.send(bytes(topic, encoding='utf-8'))
            self.number += 1
            if msg == "end":
                break

    def server_close_conn(self):
            self.conn.close()

    def server_close_tcp(self):
            self.tcp_server.close()

    def get_conn(self):
        return self.conn

    def get_addr(self):
        return self.addr












