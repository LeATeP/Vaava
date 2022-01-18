#!/bin/python3

import socket
from threading import Thread


class conn_to_main_server:
    def __init__(self) -> None:
        server_ip = ''
        addr = (server_ip, 9999)
        self.sock = socket.socket()
        self.sock.connect(addr)

        data = self.sock.recv(10).decode('utf-8')
        print(data)
        if data != 'False':
            self.unit_id = data
            
            Thread(target=self.main_loop).start()
            
            
    def main_loop(self):
        msg = b'True'
        try:
            while msg == b'True': # maintaining connection so server know that unit is alive
                msg = self.sock.recv(10)
                if msg:
                    self.sock.send(b'True')
                else:
                    print('quit')
                    quit()
            else:
                print('fail')
        except BaseException as er:
            print(er.args)
                
    
if __name__ == '__main__':
    conn_to_main_server()