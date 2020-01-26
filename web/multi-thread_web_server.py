#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
import errno

EOL1 = "\n\n"
EOL2 = "\n\r\n"

BODY = "Hello, world! --{thread_name}"

HTTP_PARMS = [
    "HTTP/1.0 200 OK",
    "Content-Type: text/plain;charset=utf-8",
    "Content-Length: {length}\r\n",
    BODY,
]

RESPONSE = "\r\n".join(HTTP_PARMS)

def handle_connection(conn, addr):
    request = ""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)  # 一次接受 1KB 请求报文
    current_thread = threading.currentThread()
    content_length = len(BODY.format(thread_name=current_thread.name))
    print request
    print "thread: {}".format(current_thread.name)
    print '-------------------------------------'
    conn.send(RESPONSE.format(thread_name=current_thread.name, length=content_length))
    time.sleep(100)  # 模拟事件阻塞
    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 套接字
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置端口复用
    ip_host = (socket.gethostname(), 8000)
    server_socket.bind(ip_host)  # 绑定服务器地址
    server_socket.listen(5)  # 设置半连接队列大小，开始监听
    server_socket.setblocking(0)  # 设置 socket 为非阻塞模式
    print 'Start listen...'
    try:
        index = 0
        while 1:
            # conn, addr = server_socket.accept()
            try:
                conn, addr = server_socket.accept()
            except socket.error as e:
                if e.args[0] == errno.EAGAIN:
                    continue
            index += 1
            current_thead = threading.Thread(target=handle_connection, args=(conn, addr), name="thread -{}".format(index))
            current_thead.start()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
