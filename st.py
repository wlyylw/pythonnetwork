from socket import *
import threading
import doc
import json
address='127.0.0.1'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12345          #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(2)     #最大连接数

def Serializ(Topic):

    return {
        "answer": Topic.answer,
        "option": Topic.option,
        "information": Topic.information
    }

class ServerThread(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.clientsock = None
            self.msg = None
            self.clientaddress = None
            self.score_list =[]
            self.TestEnd = 0
            self.path = None
        def tcplink(self,sock,addr):
            while True:
                clientsock = self.clientsock
                recvdata=clientsock.recv(buffsize).decode('utf-8')
                if len(recvdata) <= 5:
                    print("考试结束")
                    self.msg = recvdata
                    list = "用户" + str(self.clientaddress) + "得分" + recvdata
                    self.score_list.append(list)
                    break


                list_topic = doc.get_ten_topic(self.path)
                i = 0
                while recvdata == "SendTopic":
                    topic = list_topic[i]
                    topic = json.dumps(topic,default=Serializ)
                    clientsock.send(topic.encode())
                    if recvdata == "NotSendTopic":
                        print("结束发送题目")
                        break
                    i += 1
                    recvdata = clientsock.recv(buffsize).decode('utf-8')



            # clientsock.close()


        def run(self):
            print("线程开启")
            while True:
                clientsock, clientaddress = s.accept()
                self.clientsock = clientsock
                self.clientaddress = clientaddress
                print('connect from:', clientaddress)
                # 传输数据都利用clientsock，和s无关
                t = threading.Thread(target=self.tcplink, args=(clientsock, clientaddress))  # t为新创建的线程
                t.start()
                print("start")
            s.close()


        def get_address(self):
            return self.clientaddress

        def close_tcp(self):
            self.clientsock.close()
            print("线程关闭")

        def sendmsg(self,msg):
            clientsock = self.clientsock
            clientsock.send(msg.encode())

        def setPath(self,path):
            self.path = path
