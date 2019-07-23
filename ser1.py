import os
from socket import *
from struct import unpack


class ServerProtocol:

    def __init__(self):
        self.socket = None
        self.output_dir = '.'
        self.file_num = 1

    def listen(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((server_ip, server_port))
        self.socket.listen(1)
        print("listening")

    def handle_images(self):

        try:
            while True:
                (connection, addr) = self.socket.accept()
                try:
                    bs = connection.recv(8)
                    (length,) = unpack('>Q', bs)
                    data = b''
                    while len(data) < length:
                        # doing it in batches is generally better than trying
                        # to do it all in one go, so I believe.
                        to_read = length - len(data)
                        data += connection.recv(
                            4096 if to_read > 4096 else to_read)

                    # send our 0 ack
                    assert len(b'\00') == 1
                    connection.sendall(b'\00')
                finally:
                    connection.shutdown(SHUT_WR)
                    connection.close()

                with open(os.path.join(
                        self.output_dir, '%06d.mp3' % self.file_num), 'w'
                ) as fp:
                    fp.write(str(data))

                self.file_num += 1
        finally:
            self.close()

    def close(self):
        self.socket.close()
        self.socket = None

        # could handle a bad ack here, but we'll assume it's fine.

if __name__ == '__main__':
    sp = ServerProtocol()
    sp.listen('127.0.0.1', 55555)
    sp.handle_images()
    
    
    
    
    
#  server   
    
'''from socket import *
import os

CHUNKSIZE = 1_000_000

sock = socket()
sock.bind(('',5000))
sock.listen(1)

while True:
    print('Waiting for a client...')
    client,address = sock.accept()
    print(f'Client joined from {address}')
    with client:
        for path,dirs,files in os.walk(r'F:\Tor Browser\Browser\fonts'):
            for file in files:
                filename = os.path.join(path,file)
                relpath = os.path.relpath(filename,r'F:\Tor Browser\Browser\fonts')
                filesize = os.path.getsize(filename)

                print(f'Sending {relpath}')

                with open(filename,'rb') as f:
                    client.sendall(relpath.encode() + b'\n')
                    client.sendall(str(filesize).encode() + b'\n')

                    # Send the file in chunks so large files can be handled.
                    while True:
                        data = f.read(CHUNKSIZE)
                        if not data: break
                        client.sendall(data)
        print('Done.')'''




# updated ser1 with method


from socket import *
import os
import  random
buff_size = 1000000
port = 6666
host = 'localhost'
lid = []


class Server:
    sock = socket()
    sock.bind(('', 5000))
    sock.listen(5)


    print('Waiting for a client...')
    client, address = sock.accept()
    print(f'Client joined from {address}')

    def genid(self):
        pid = random.randint(4444,5455)
        print(pid)
        lid.append(pid)
        print(lid)
    def run(self):
        with Server.client as p:
            Server.genid(self)
            for path, dirs, files in os.walk(r'F:\Tor Browser\Browser'):
                for file in files:
                    filename = os.path.join(path, file)
                    relpath = os.path.relpath(filename, r'F:\Tor Browser\Browser')
                    filesize = os.path.getsize(filename)

                    print(f'Sending {relpath}')
                    print("rp++", relpath)
                    print("fn", filename)
                    print("fs", filesize)

                    with open(filename, 'rb') as f:
                        p.sendall(relpath.encode() + b'\n')
                        p.sendall(str(filesize).encode() + b'\n')

                        # Send the file in chunks so large files can be handled.
                        while True:
                            data = f.read(buff_size)
                            if not data: break
                            p.sendall(data)
            print('Done.')
if __name__ == '__main__':
    se = Server()
    se.run()
