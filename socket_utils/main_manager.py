#!/bin/python3

import socket



sock = socket.socket()
addr = ('0.0.0.0', 8080)  # ip will change to 'main_server' after main_server container is created
sock.bind(addr)

print(f'listening to {addr}')
sock.listen()
conn, addr = sock.accept()

print(f"Connected by: {addr}")
while True:
    data = conn.recv(1024)
    if data:
        print(f"received {data} \nsending back response...")
        msg_back = f"You send: {data}"
        msg_bytes = bytes(msg_back, 'utf-8')
        conn.sendall(b"received")
