import socket
import random
import os


# def dwld(path):
#     randomPort = random.randint(3000,50000)
#     dwldSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     dwldSocket.bind(("127.0.0.1",randomPort))
#     dwldSocket.listen(5)

#     connection.send(str(randomPort).encode())
#     while 1 :

#         dateSocket,address = dwldSocket.accept()

#         with open(path, "rb") as file_to_send:
#             data = file_to_send.read()
#             dateSocket.sendall(data)
#         dateSocket.close()
#         break
#     print('ASasASas')

#     dwldSocket.close()


appSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

appSocket.bind(("127.0.0.1",2121))
appSocket.listen(5)

#listen for connection
connection,client = appSocket.accept()
print('connexted: ',client)

while True:
    msg = connection.recv(1024).decode()
    command,path = msg.split(' ')
    command=command.lower()
    print("Recieved: ",msg)

appSocket.close()

