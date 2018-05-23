#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

import socket
import time
import threading

# 指定协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9991))
server.listen(2)


def deal_thread(s, addr):
    print('a client link from %s:%s' % addr)
    s.send(b'welcome!')
    while True:
        data = s.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        s.send(('hello %s' % data.decode('utf-8')).encode('utf8'))
        print(data.decode('utf-8'))
    s.close()
    print('connect from %s:%s closed' % addr)


while True:
    s, addr = server.accept()
    deal_thread = threading.Thread(target=deal_thread, args=(s, addr))
    deal_thread.start()

# client
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 9999))
# print(client.recv(1024).decode('utf-8'))
# client.send()
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     client.send(data)
#     print(client.recv(1024).decode('utf-8'))
# client.send(b'exit')
# client.close()