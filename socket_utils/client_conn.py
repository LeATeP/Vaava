#!/bin/python3

import socket

addr = ('172.18.0.4', 8080)

sock = socket.socket()
sock.connect(addr)

while True:
    msg = bytes(input(), 'utf-8')
    sock.sendall(msg)

    data = sock.recv(1024)
    if data:
        print(data)