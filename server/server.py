import socket
import random
import json
import os


def getFolderSize(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def Help():
    return "HELP              :  SHOW THIS HELP\nLIST              :  LIST FILES\nPWD               :  SHOW CURRENT DIR\nCD dir_name       :  CHANGE DIRECTORY\nDWLD file_path    :  DWNLOAD FILE\nCLEAR             :  CLEAR TERMINAL\nQUIT              :  EXIT\n"


def List():
    sizeAllFile = 0
    arr = []
    ldr = os.listdir(Pwd())
    for i in ldr:
        p = []
        size = getFolderSize(f"{Pwd()}\{i}") if os.path.isdir(
            i) else os.stat(i).st_size
        p.append(i)
        p.append(os.path.isdir(i))
        p.append(size)
        arr.append(p)
        sizeAllFile += size
    arr.append(sizeAllFile)
    return json.dumps(arr)


def Pwd():
    return os.getcwd()


def Cd(folder):
    os.chdir(folder)
    return f"Directory change to {folder}"


appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.bind(("127.0.0.1", 2121))
appSocket.listen(1)

# listen for connection
# connection, client = appSocket.accept()

# print(client, "connected")

while True:
    connection, client = appSocket.accept()
    data = connection.recv(64).decode().split(" ")
    data[0] = data[0].lower()
    print("Recieved: ", data)

    if data[0] == "!":
        break

    elif data[0] == "help":
        connection.send(Help().encode())

    elif data[0] == "list":
        connection.send(List().encode())

    elif data[0] == "pwd":
        connection.send(Pwd().encode())

    elif data[0] == "cd":
        connection.send(Cd(data[1]).encode())
