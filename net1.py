from socket import *
import doc
import  json
import random

number =0
def Serializ(Topic):
    return {
        "answer" : Topic.answer,
        "option" : Topic.option,
        "information" : Topic.information
    }



ip_port = ('127.0.0.1', 8080)
back_log = 40
buffer_size = 1024
TOPIC_NUMBER=10 #题目数
list = doc.clissfy("E:\\Desktop\\kstk.docx")    #获取已经处理好的word文档中的信息
MAX_TOPIC = len(list)
random_list = random.sample(range(0,MAX_TOPIC), TOPIC_NUMBER)
print(random_list)

class server_operator():
    def tcp_operator(self):
        tcp_server = socket(AF_INET, SOCK_STREAM)
        tcp_server.bind(ip_port)
        tcp_server.listen(back_log)
        conn, addr = tcp_server.accept()  # 服务器阻塞
        self.addr =addr #客户端地址
        self.conn = conn#双向连接
    def __init__(self):
        self.number =0 #题目计数

    def pre_start_test(self):
        while True:
            data = self.conn.recv(buffer_size)  # 收缓存为空，则阻塞
            msg = data.decode('utf-8')
            print('客户端发来的消息是', msg)
            topic = list[random_list[self.number]]  # 随机10题
            topic = json.dumps(topic, default=Serializ)
            self.conn.send(bytes(topic, encoding='utf-8'))
            self.number += 1
            # print("number: ", self)
            # print('双向链接是', self.conn)


            if msg =="end":
                break
    def server_close_conn(self):
            self.conn.close()
    def server_close_tcp(self):
            self.tcp_server.close()
    def get_conn(self):
        return self.conn
    def get_addr(self):
        return self.addr












