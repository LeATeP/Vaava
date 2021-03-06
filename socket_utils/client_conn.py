#!/bin/python3

import socket
from threading import Thread


class conn_to_main_server:
    def __init__(self) -> None:
        self.running = True
        server_ip = 'main_server'
        addr = (server_ip, 9999)
        self.sock = socket.socket()
        self.sock.setblocking(1)
        self.sock.connect(addr)

        data = self.sock.recv(10).decode('utf-8')
        print(data)
        if data != 'False':
            self.unit_id = data
            Thread(target=self.main_loop, daemon=True).start()
        else:
            print('no data from server')
            quit()
            
            
    def main_loop(self):
        try:
            while self.running == True: # maintaining connection so server know that unit is alive
                msg = self.sock.recv(10)
                if msg == b'True':
                    self.sock.send(b'True')
                    continue
                break
            print('raising exception')
            raise BaseException
        except BaseException as er:
            self.running = False
            print(er.args)
            quit()
                
    
if __name__ == '__main__':
    conn_to_main_server()