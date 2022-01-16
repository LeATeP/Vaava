#!/bin/python3

from base64 import decode
import socket
from threading import Thread
from time import sleep



class conn_to_main_server:
    def __init__(self) -> None:
        server_ip = ''
        addr = (server_ip, 9999)
        self.sock = socket.socket()
        self.sock.connect(addr)

        data = self.sock.recv(10).decode('utf-8')
        
        if data != 'False':
            self.unit_id = int(data)
            
            msg = b'True'
            while msg == b'True': # maintaining connection so server know that unit is alive
                msg = self.sock.recv(10)
                print(msg)
    
    
if __name__ == '__main__':
    conn_to_main_server()