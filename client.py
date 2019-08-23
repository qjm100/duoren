
# -*- coding: UTF-8 -*-
import socket, threading
 
 
# 创建客户端对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 目标主机
host = input('输入目标ip')
 
while True:
    name = input('请输入个人昵称， 不得超过十个字符，少于一个字符')
    if 1<len(name)<10:
        break
 
# 目标端口
port = 9090
 
# 连接客户端
client.connect((host, port))
print('-'*5+'已连接到服务器'+'-'*5)
print('-'*5+'输入enter关闭与服务器的连接'+'-'*5)
 
 
def outdatas():
    while True:
 
        # 输入要发给服务器的信息
        outdata = input('')
        print()
        if outdata=='enter':
            break
        # 发送给服务器
        client.send(f'{name}:{outdata}'.encode('utf-8'))
        print('%s:%s'% (name, outdata))
 
 
def indatas():
 
    while True:
        # 接受来自服务器的信息
        indata = client.recv(1024)
 
        # 将接受到的信息，进行编码
        print(indata.decode('utf-8'))
 
 
# 建立多线程
# 建立接受信息，线程对象
t1 = threading.Thread(target=indatas, name='input')
 
# 建立输出信息，线程对象
t2 = threading.Thread(target=outdatas, name='out')
 
# 启动多线程
t1.start()
t2.start()
 
# 阻塞线程，直到子线程执行结束，主线程才能结束。
# t1.join()
t2.join()
 
# 关闭连接
print('-'*5+'服务器断开连接'+'-'*5)
client.close()

