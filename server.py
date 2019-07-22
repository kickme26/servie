# server2.py
import socket
from threading import Thread
import threading
import os

host = 'localhost'
port = 6666
buff_size = 1024


class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        self.ide = ''
        print(" New thread started for " + ip + ":" + str(port))
        print(f"Your ID is:{str(self.ide)} ")

    def run(self):
        filename = 'mytext.txt'
        f = open(filename, 'rb')
        while True:
            l = f.read(buff_size)
            while (l):
                self.sock.send(l)
                # print('Sent ',repr(l))
                l = f.read(buff_size)

            if not l:
                f.close()
                self.sock.close()
                break

    def prid(self):
        ide = os.getpgid()
        id_list.append(ide)
        print("£££££££££££££££")
        print(ide)

        return ide


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((host, port))
threads = []
id_list = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    print('Got connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
    for t in threads:
        t.join()
    print()
    print(threads)
