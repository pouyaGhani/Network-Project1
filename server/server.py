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


def Help():
    return "help -> Display a list of commands\nlist -> List of files and their size in a directory\ndwld -> Download files\npwd -> Our current location in a directory\ncd -> Change directory"


def List():
    sizeAllFile = 0
    arr = []
    ldr = os.listdir(Pwd())
    for i in ldr:
        p = []
        size = os.stat(i).st_size
        p.append(i)
        p.append(os.path.isdir(i))
        p.append(size)
        arr.append(p)
        sizeAllFile += size
    arr.append(sizeAllFile)
    return arr


def Pwd():
    return os.getcwd()


appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.bind(("127.0.0.1", 2121))
appSocket.listen(1)

# listen for connection
connection, client = appSocket.accept()

print(client, "connected")

while True:
    data = connection.recv(64).decode().split(" ")
    data[0] = data[0].lower()
    print("Recieved: ", data)

    if data[0] == "!":
        break
    elif data[0] == "help":
        Help()
    elif data[0] == "list":
        List()
    elif data[0] == "pwd":
        Pwd()

connection.close()
