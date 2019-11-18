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

def get_topic():
    while True:
        list = []
        for i in range(0, 11):
            if i == 10:
                msg = "NG"
                s.close()
                return list
            else:
                msg = "YG"
                s.send(msg.encode())
                recvdata = s.recv(buffsize).decode('utf-8')
                recvdata = json.loads(recvdata, object_hook=DeSerializ)
                topic = doc.Topic(recvdata.information, recvdata.answer, recvdata.option)
                list.append(topic)

            # TODO:结束考试后退出程序的逻辑
        # senddata = input('想要发送的数据：')
        # if senddata=='exit':
        #     break
        # s.send(senddata.encode())
list =get_topic()

for i in range(0,len(list)):
    print(list[i].answer)
