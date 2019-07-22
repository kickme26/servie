
# client.py
import socket

host = 'localhost'
port = 6666
buff_size = 104


class Client():
    def option(self):
        print("Enter the option to perform: \n1.Launce \n2.Trace")
        option = int(input(">>>   "))

        if option == int(1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            with open('received_file', 'wb') as f:
                print('file opened')
                while True:
                    # print('receiving data...')
                    data = s.recv(100)
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
