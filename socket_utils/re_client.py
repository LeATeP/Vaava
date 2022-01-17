#!/bin/python3

import socket
from time import sleep
import json

class Client:
    def __init__(self) -> None:
        self.addr = ('', 9999)
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.addr)


        while True:
            try:
                data = self.sock.recv(10).decode('utf-8')
                print(data)
            except KeyboardInterrupt:
                print(':: trigerred interrupt')
                self.sock.send(json.dumps(list(self.addr)).encode('utf-8'))
                print(':: sent data')
                break

        # if data != 'False':
        #     self.unit_id = int(data)

        #     msg = b'True'
        #     while msg == b'True':  # maintaining connection so server know that unit is alive
        #         msg = self.sock.recv(10)
        #         print(msg)


if __name__ == '__main__':
    Client()
