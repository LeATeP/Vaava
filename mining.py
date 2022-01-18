#!/bin/env python3
from os import environ
from sys import path
from random import randint
from time import sleep

env = environ.get
path.append(env("vaava"))
from sql.sql_query import psql
from utils.colors import fg_rgb
from socket_utils.client_conn import conn_to_main_server

class mining(psql, conn_to_main_server):
    def __init__(self) -> None:
        psql.__init__(self)
        conn_to_main_server.__init__(self)
        self.host_name = env('HOSTNAME')
        
        self.exec(f'''
                  update unit 
                  set state = 'mining', container_id = '{self.host_name}'
                  where id = {self.unit_id};''')

    def start_work(self):
        try:
            while self.running:
                sleep(1)
                
                drop = self.gen_drop()
                print(drop)
                for item in drop:
                    res = self.exec(f'''update items
                    set amount = amount + {drop[item]}
                    where name = '{item}';''')
                    if not res:
                        self.running = False 
            print('probably storage is full')
            raise BaseException
        except BaseException as error:
            print(error.args)
        
    def gen_drop(self):
        drop =  {'rock': randint(1,2) if randint(1, 10) > 5 else None,
                'energy_rock': 1 if randint(1, 10) > 8 else None,
                'iron_ore': 1 if randint(1, 100) > 95 else None}

        drop = {n: drop[n] for n in drop if drop[n] is not None}
        return drop
        


if __name__ == "__main__":
    mining().start_work()
        






