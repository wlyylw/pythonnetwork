import doc
from socket import *
import  json

def DeSerializ(t):
    return doc.Topic(
         t["information"],
         t["answer"],
         t["option"]
    )
ip_port = ('127.0.0.1', 8080)
back_log = 40
buffer_size = 1024
class client_operator:

    def __init__(self):
        pass

    def tcp_operator(self):
        self.tcp_client = socket(AF_INET, SOCK_STREAM)
        self.tcp_client.connect(ip_port)

    def pre_start_test(self):
            # msg=input('>>:').strip()  #去掉空格
            # msg = input('>>:')          #发送空格到自己的发送缓存中
            msg ="start"
            for i in range(0,10):
                self.tcp_client.send(msg.encode('utf-8'))
                print('客户端已经发送消息')
                data = self.tcp_client.recv(buffer_size)  #收缓存为空则阻塞
                data=data.decode('utf-8')
                data = json.loads(data,object_hook=DeSerializ)
                print('题目: ',data.information)
                print('选项: ', data.option)
                print('答案: ',data.answer)

    def tcp_operator_close(self):
        self.tcp_client.close()