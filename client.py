# client2.py
# !/usr/bin/env python

import socket

TCP_IP = 'localhost'
TCP_PORT = 6666
BUFFER_SIZE = 104


class Client():
    def option(self):
        print("Enter the option to perform: \n1.Launce \n2.Trace")
        option = int(input(">>>   "))

        if option == int(1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            with open('received_file', 'wb') as f:
                print('file opened')
                while True:
                    # print('receiving data...')
                    data = s.recv(BUFFER_SIZE)
                    print('data=%s', (data))
                    if not data:
                        f.close()
                        print('file close()')
                        break
                    # write data to a file
                    f.write(data)
            print('Successfully get the file')
            s.close()
            print('Connection closed')

        elif option == int(2):
            print("Enter the ID to Trace  :")
            ide = int(input(">>>  "))
            print(ide)


        else:
            print("You entered th wrong one")


while True:
    c = Client()
    c.option()
