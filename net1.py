from socket import *
import doc
import  json
import random
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


tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

print('服务端开始运行了')

list = doc.clissfy()    #获取已经处理好的word文档中的信息
MAX_TOPIC = len(list)
random_list = random.sample(range(0,MAX_TOPIC), TOPIC_NUMBER)
print(random_list)


conn, addr = tcp_server.accept()  #服务器阻塞
print('双向链接是', conn)
print('客户端地址', addr)


while True:
    data = conn.recv(buffer_size)    #收缓存为空，则阻塞
    print('客户端发来的消息是', data.decode('utf-8'))
    # conn.send(data.upper())
    for i in range (0,TOPIC_NUMBER):
        topic = list[random_list[i]]  #随机10题
        topic = json.dumps(topic, default=Serializ)
        conn.send(bytes(topic, encoding='utf-8'))
conn.close()

tcp_server.close()
