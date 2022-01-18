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
                                        order by id limit 1;''')
        unit = self.fetch_dict()
        print(unit)
        if not unit:
            conn.send(b'False')
            return
        
        
        unit_id = str(unit[0]['id'])
        self.thread_dict[unit_id] = True
        
        self.exec(f'''update unit set state = 'working' where id = '{unit_id}';''')

        encoded = bytes(unit_id, 'utf-8')
        conn.send(encoded); sleep(0.1) # sleep to interrupt continuous sending data / mixing up

        while self.thread_dict[unit_id] == True:
            try:
                conn.send(b'True')
                
                sleep(0.1) # to give client time to send msg back (not necessary)
                send_confirmation = conn.recv(10)
                if send_confirmation == b'True':
                    print(f'{unit_id}, {self.thread_dict[unit_id]} good')
                    sleep(1) # 1 check per sec is enough
                    continue
                raise Exception
            except Exception as er:
                print('error', er)
                self.thread_dict[unit_id] = False
        else: # if False, inform server to terminate
            self.thread_dict.pop(unit_id)
            self.default_sql_unit_data(unit_id)
            return
        
    def default_sql_unit_data(self, unit_id):
        self.exec(f'''
                  update unit 
                  set state = 'idle', container_id = null
                  where id = {unit_id};''')
            
            


if __name__ == "__main__":    
    Manager()
    