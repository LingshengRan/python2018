# -*- coding: utf-8 -*-
"""
Created on 2021/9/27 14:56

@author: R.ls
"""

import socket

def send_file_2client(new_client_socket, client_addr):
    # 需要下载的文件
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端请求下载文件：%s" % file_name)

    file_content = None
    # 打开文件 读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as e:
        print("没有要下载的文件：%s" % file_name)

    if file_content:
        new_client_socket.send(file_content)

def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口
    tcp_server_socket.bind(("", 7890))

    # 监听 128 同时链接
    tcp_server_socket.listen(128)

    while True:
        print("监听客户端链接...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("成功链接客户端：%s" % str(client_addr))

        # 接收客户端发送过来的消息
        send_file_2client(new_client_socket, client_addr)

        # 关闭套接字
        new_client_socket.close()
        print("已经服务完毕，等待下一个客户端...")

    # 关闭服务器
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

