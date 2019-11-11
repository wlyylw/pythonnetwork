#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige
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
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>:')          #发送空格到自己的发送缓存中
    # msg=input('>>:').strip()  #去掉空格
    tcp_client.send(msg.encode('utf-8'))
    print('客户端已经发送消息')
    data = tcp_client.recv(buffer_size)  #收缓存为空则阻塞
    data=data.decode('utf-8')
    data = json.loads(data,object_hook=DeSerializ)
    print('收到服务端发来的消息是', data.option)
    print(data.answer)
    print(data.information)
tcp_client.close()