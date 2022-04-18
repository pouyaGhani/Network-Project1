import socket
import random
import os


def Cd(folder):
    os.chdir(folder)



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
        connection.send(Help().encode())
    elif data[0] == "list":
        List()
    elif data[0] == "pwd":
        Pwd()
    elif data[0] == "cd":
        Cd(data[1])

connection.close()
