#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

EOL1 = "\n\n"
EOL2 = "\n\r\n"

BODY = "Hello, world!"

HTTP_PARMS = [
    "HTTP/1.0 200 OK",
    "Content-Type: text/plain;charset=utf-8",
    "Content-Length: {}\r\n".format(len(BODY)),
    BODY,
]

RESPONSE = "\r\n".join(HTTP_PARMS)

def handle_connection(conn, addr):
    request = ""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)  # 一次接受 1KB 请求报文
    print request
    print '-------------------------------------'
    conn.send(RESPONSE)
    time.sleep(100)  # 模拟事件阻塞
    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 套接字
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置端口复用
    ip_host = (socket.gethostname(), 8000)
    server_socket.bind(ip_host)  # 绑定服务器地址
    server_socket.listen(5)  # 设置半连接队列大小，开始监听(PS:然而单线程模式下这个东西并没有什么卵用~)
    print 'Start listen...'
    try:
        while 1:
            conn, addr = server_socket.accept()
            handle_connection(conn, addr)
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

