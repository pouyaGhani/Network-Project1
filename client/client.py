import socket
import os

def dwld(path):
    print('asd')
    receivedPort = appSocket.recv(1024).decode()
    dwldSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    dwldSocket.connect(("127.0.0.1",int(receivedPort)))
    print(receivedPort)
    with open(path, 'wb') as file_to_write:
        while True:
            data = dwldSocket.recv(1024)
            if not data:
                break
            file_to_write.write(data)
        file_to_write.close()
    dwldSocket.close()


appSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connection
appSocket.connect(("127.0.0.1",2121))

while(True):
    msg=input()
    command,path=msg.split(' ')
    try:
        appSocket.send(msg.encode())
        if command.lower() == "dwld":
            dwld(path)

    except:
        print("connection Lost!")
        break


appSocket.close()
