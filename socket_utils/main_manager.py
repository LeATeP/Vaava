#!/bin/python3

import socket
from threading import Thread
from os import environ
from sys import path
from time import sleep

env = environ.get
path.append(env("vaava"))
from sql.sql_query import psql



class Manager(psql):
    def __init__(self) -> None:
        psql.__init__(self)
        self.thread_dict = {}
        
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
            Thread(target=self.create_thread, args=(conn,), daemon=True).start()
            
            # creating thread, for new client

            
 
 
 
 
 
 
 
 
 
            
    def create_thread(self, conn):
        check_available_unit = self.exec('''
                                        select id from unit 
                                        where state = 'idle' and fraction = 'Main'
                                        limit 1;''')
        unit = self.fetch_dict()
        print(unit)
        if not unit:
            conn.sendall(b'False')
            return
        
        unit_id = str(unit[0]['id'])
        self.thread_dict[unit_id] = True
        
        encoded = bytes(unit_id, 'utf-8')
        conn.sendall(encoded)

        while self.thread_dict[unit_id] == True:
            try:
                conn.sendall(b'True')
                sleep(1)
                print('good')
            except Exception as er:
                print('fail', er)
                self.create_thread[unit_id] == False
                break # if client is broken, break loop, and no else continuation 
        else: # if False, inform server to terminate
            conn.sendall(b'False')
            return
            
            


if __name__ == "__main__":    
    Manager()
    