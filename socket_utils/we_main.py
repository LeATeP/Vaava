#!/bin/python3

import json
import socket
from threading import Thread
from time import sleep
import time


class Server():
    def __init__(self) -> None:
        self.clients = []
        self.running_threads = {}
        self.init_server()

    def init_server(self) -> None:

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ('', 9999)
        server_socket.bind(addr)

        print(f'listening on {addr}')
        # receiver_thread = Thread(
        #     target=self.server_receiver,
        #     args=(server_socket, ),
        #     daemon=True
        # )
        server_socket.listen()

        while True:
            conn, addr = server_socket.accept()
            print(f"accepted connection from: {addr}")
            self.clients.append((conn, addr, ))
            thread = Thread(
                target=self.client_handler,
                args=(conn, addr,),
                daemon=True
            )
            thread.start()
            self.running_threads[addr] = thread

    def client_handler(self, conn, addr):
        while True:
            try:
                conn.sendall(b'True')
                print(f'sent {True!r}')
                sleep(1)
            except ConnectionAbortedError:
                print(': connection aborted')
                for client in self.clients:
                    if client[1] == addr:
                        client[0].close()
                        self.clients.remove(client)
                        del self.running_threads[addr]
                        print(': cleaned up closed thread')
                break


if __name__ == "__main__":
    Server()
