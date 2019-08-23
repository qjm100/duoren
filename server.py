
 
 
# auther: kele
# 创建时间：2019/1/3 18:42
 
 
# 导入socket包
import socket, threading
 
# 创建一个socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 获取本地ip
host = socket.gethostname()
 
# 给定端口
port = 9090
 
# 给服务器IP和端口
server.bind((host, port))
 
# 最大连接数
server.listen(5)
 
print('输入enter退出服务器')
 
# 创建一个客户端列表
clients = list()
# 存放已经创建线程的客户端
end = list()
 
 
# 阻塞式等待客户端连接，返回连接对象，与间接对象地址
def accept():
 
    while True:
        client, addr = server.accept()
        clients.append(client)
        print("\r"+'-'*5+f'服务器被{addr}连接: 当前连接数：-----{len(clients)}'+'-'*5, end='')
 
 
def recv_data(client):
    while True:
        # 接受来自客户端的信息
        try:
            indata = client.recv(1024)
        except Exception as e:
            clients.remove(client)
            end.remove(client)
            print("\r" + '-' * 5 + f'服务器被断开: 当前连接数：-----{len(clients)}' + '-' * 5, end='')
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            # 转发来自客户端的信息，发给其他客户端
            if clien != client:
                clien.send(indata)
 
 
def outdatas():
    while True:
 
        # 输入要给客户端的信息
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            break
        print('发送给所有人:%s'% outdata)
        # 给每个客户端发信息
        for client in clients:
                client.send(f"服务器:{outdata}".encode('utf-8)'))
 
 
def indatas():
    while True:
        # 循环出连接的客户端，并创建相应线程
            for clien in clients:
                # 若是线程已经存在则跳过
                if clien in end:
                    continue
                index = threading.Thread(target = recv_data,args = (clien,))
                index.start()
                end.append(clien)
 
 
# 建立多线程
# 创建接受信息，线程对象
t1 = threading.Thread(target = indatas,name = 'input')
t1.start()
 
# 创建发送信息，线程对象
 
t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()
 
# 等待客户连接，线程对象
 
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()
 
# t1.join()
t2.join()
 
# 关闭每一个服务器
for client in clients:
    client.close()
print('-'*5+'服务器断开连接'+'-'*5)


