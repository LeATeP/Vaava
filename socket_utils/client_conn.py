#!/bin/python3

import socket
from threading import Thread



class conn_to_main_server:
    def __init__(self) -> None:
        server_ip = ''
        addr = (server_ip, 9999)

        self.sock = socket.socket()
        self.sock.connect(addr)

        unit_id = self.sock.recv(1024)
        if unit_id:
            Thread(target=self.wait_signals).start()


    def wait_signals(self):
        # get unit_id to associate yourself with
        pass