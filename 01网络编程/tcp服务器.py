# -*- coding: utf-8 -*-
"""
Created on 2021/9/27 14:56 

@author: R.ls
"""

import socket

# tcp 严格区分客户端和服务端
def socket_chat():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    tcp_server_socket.bind(("", 7890))

    # 监听
    tcp_server_socket.listen(128)

    while True:
        print("监听客户端链接...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("成功链接客户端：%s" % str(client_addr))

        while True:
            # 接收客户端发送过来的消息
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的消息：%s" % recv_data.decode("gbk"))

            if recv_data:
                new_client_socket.send("服务器收到消息！！！".encode("gbk"))
            else:
                break

        # 关闭套接字
        new_client_socket.close()
        print("已经服务完毕，等待下一个客户端...")

    # 关闭服务器
    tcp_server_socket.close()


if __name__ == "__main__":
    socket_chat()

