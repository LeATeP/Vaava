#!/bin/python3

import socket
from threading import Thread
from time import sleep



class conn_to_main_server:
    def __init__(self) -> None:
        server_ip = ''
        addr = (server_ip, 9999)

        self.sock = socket.socket()
        self.sock.connect(addr)

        unit_id = self.sock.recv(10)
        print(unit_id)
        
        msg = ''
        while msg != b'False':
            msg = self.sock.recv(10)
            print(msg)
        # if unit_id:
            # Thread(target=self.wait_signals).start()


    def maintaining_connection(self):
        # get unit_id to associate yourself with
        pass
    
    
if __name__ == '__main__':
    conn_to_main_server()