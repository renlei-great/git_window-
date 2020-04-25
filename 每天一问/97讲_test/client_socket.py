import socket

# 创建socket
cli_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
cli_server.connect(('192.168.223.1', 8000))
# cli_server.bind()
while True:
    # 发送数据
    re_data = input('请输入要发送的内容：')
    if re_data == 'exit':
        # 关闭连接
        cli_server.close()
        break
    cli_server.send(re_data.encode())
    data = cli_server.recv(1024).decode()
    print(data)
