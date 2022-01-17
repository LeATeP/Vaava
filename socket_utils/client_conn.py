#!/bin/python3

import socket

class conn_to_main_server:
    def __init__(self) -> None:
        server_ip = 'main_server'
        addr = (server_ip, 9999)
        self.sock = socket.socket()
        self.sock.connect(addr)

        data = self.sock.recv(10).decode('utf-8')
        
        if data != 'False':
            self.unit_id = int(data)
            
            msg = b'True'
            while msg == b'True': # maintaining connection so server know that unit is alive
                msg = self.sock.recv(10)
                if msg:
                    self.sock.send(b'True')
                    print(msg)
    
    
if __name__ == '__main__':
    conn_to_main_server()