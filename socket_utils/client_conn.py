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

        unit_id = self.sock.recv(1024)
        print(unit_id)
        while True:
            msg = self.sock.recv(255)
            # sleep(100)
        # if unit_id:
            # Thread(target=self.wait_signals, daemon=True).start()


    def maintaining_connection(self):
        # get unit_id to associate yourself with
        pass
    
    
if __name__ == '__main__':
    conn_to_main_server()