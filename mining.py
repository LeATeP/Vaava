#!/bin/env python3
from os import environ
from sys import path
from random import randint
from time import sleep

env = environ.get
path.append(env("GAME")) # my_whatever/game_docker
from sql.sql_query import psql
from utils.colors import fg_rgb

class mining(psql):
    def __init__(self) -> None:
        psql.__init__(self)
        # self.host_name = env('HOSTNAME')

    def start_work(self):
        try:
            self.exec('''select id from unit
                       where state = 'idle' limit 1;''')
            data = self.fetch_dict()
            # if no worker are available then break
            if not data:
                raise Exception('no worker are Free')

            # change worker status on True
            id = data[0]['id']
            self.exec(f'''update unit set state = 'mining'
                        where id = {id} returning state;''')
                
            
            good = True    
            while good:
                sleep(0.1)
                drop = self.gen_drop()
                print(drop)
                for item in drop:
                    res = self.exec(f'''update items
                    set amount = amount + {drop[item]}
                    where name = '{item}';''')
                    if not res:
                        good = False; continue


                
                
                
        except (Exception) as error:
            print(error.args)
        
    def gen_drop(self):
        drop =  {'rock': randint(1,2) if randint(1, 10) > 5 else None,
                'energy_rock': 1 if randint(1, 10) > 8 else None,
                'iron_ore': 1 if randint(1, 100) > 95 else None}

        drop = {n: drop[n] for n in drop if drop[n] is not None}
        return drop
        


if __name__ == "__main__":
    mining().start_work()
        






