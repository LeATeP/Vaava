#!/bin/python3

import socket
from threading import Thread
from os import environ
from sys import path

env = environ.get
path.append(env("vaava"))
from sql.sql_query import psql



class Manager(psql):
    def __init__(self) -> None:
        psql.__init__(self)

        self.exec('''
                  update unit 
                  set state = 'idle', container_id = null 
                  where fraction = 'Main';''')
        
        self.init_server()

    def init_server(self) -> None:
        sock = socket.socket()
        addr = ('0.0.0.0', 9999)  # ip will change to 'main_server' after main_server container is created
        sock.bind(addr)
        
        print(f'listening to {addr}')
        sock.listen()

        while True:
            conn, addr = sock.accept()
            print(f"Connected by: {addr}")
            Thread(target=self.create_thread, args=(conn,)).start()
            # creating thread, for new client
            
    def create_thread(self, conn):
        check_available_unit = self.exec('''
                                        select id from unit 
                                        where state = 'idle' and fraction = 'Main'
                                        limit 1;''')
        unit = self.fetch_dict()
        print(unit)
        if unit:
            id = str(unit[0]['id'])
            encoded = bytes(id, 'utf-8')
            conn.sendall(encoded)
        else:
            no_msg = bytes('no', 'utf-8')
            conn.sendall(no_msg)
            
        # while True:
            # data = conn.recv(1024)
            # if data:
                

Manager()
    
# while True:
    # data = conn.recv(1024)
    # if data:
        # print(f"received {data} \nsending back response...")
        # msg_back = f"You send: {data}"
        # msg_bytes = bytes(msg_back, 'utf-8')
        # conn.sendall(b"received")
