import socket
import threading

def socket_worker(socket, address):
    """处理子客户端请求"""
    print(address, '接入成功')
    while True:
        data = socket.recv(1024).decode()
        print(address,":"+ data)
        print(address, ':请输入要发送的内容:', end='')
        re_data = input()
        socket.send(re_data.encode())


# 建立socket
sok_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
sok_server.bind(('0.0.0.0', 8000))
# 调为被动接受
sok_server.listen()
# 调为阻塞状态，等待新的连接
print('---等待接入')
# 进行多任务
while True:
    # 调为阻塞状态，等待新的连接
    new_socket, address = sok_server.accept()

    # 为此客户端分配线程去服务进行服务
    threading.Thread(target=socket_worker, args=(new_socket, address)).start()

# 关闭连接
sok_server.close()