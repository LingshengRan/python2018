# -*- coding: utf-8 -*-
"""
Created on 2021/9/27 14:56

@author: R.ls
"""

import socket


# udp聊天器

def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input("对方ip：")
    dest_port = int(input("对方端口："))
    send_data = input("发送消息：")
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收信息"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def socket_chat():
    # 创建udp的套接字 AF_INET:ipv4
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 7788))

    # 发送和接收数据
    while True:
        # 发送
        send_msg(udp_socket)
        # 接收并显示
        recv_msg(udp_socket)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    socket_chat()
