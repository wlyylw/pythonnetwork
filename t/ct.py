#客户端与上一个没有任何改变
from socket import *
import doc
import json

address='127.0.0.1'   #服务器的ip地址
port=12345           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))

def DeSerializ(t):
    return doc.Topic(
         t["information"],
         t["answer"],
         t["option"]
    )


class ClientThread():

    def __init__(self):
        self.recvdata = None
        self.TestEnd = None # 考试还没结束

    def get_topic(self):
        while True:
            list = []
            #这一段执行一次  客户端第一次请求的时候调用
            for i in range(0, 11):
                if i == 10:
                    msg = "NotSendTopic"
                else:
                    msg = "SendTopic"
                    s.send(msg.encode())
                    recvdata = s.recv(buffsize).decode('utf-8')
                    recvdata = json.loads(recvdata, object_hook=DeSerializ)
                    topic = doc.Topic(recvdata.information, recvdata.answer, recvdata.option)
                    list.append(topic)
                    self.recvdata = recvdata
                # TODO:结束考试后退出程序的逻辑
            return list
        #TODO：
        s.close()
    def send_msg(self,msg):
        s.send(msg.encode())


    # def isTestEnd(self):
    #     # self.recvdata = s.recv(buffsize).decode('utf-8')
    #     if self.recvdata == "TestEnd":
    #         self.TestEnd = 1
    #     else:
    #         self.TestEnd = 0
    #         # 即 考试已经结束
