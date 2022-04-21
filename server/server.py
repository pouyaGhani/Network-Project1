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
    ldr = os.listdir(os.getcwd())
    for i in ldr:
        p = []
        size = getFolderSize(f"{os.getcwd()}\{i}") if os.path.isdir(
            i) else os.stat(i).st_size
        p.append(i)
        p.append(os.path.isdir(i))
        p.append(size)
        arr.append(p)
        sizeAllFile += size
    arr.append(sizeAllFile)
    return json.dumps(arr)


def Pwd():
    loc = f"{os.getcwd()}\\"
    i = loc.find("files")
    return loc[i+5:] if i != -1 else "\\"


def Cd(folder, location):
    folder = folder.replace("/", "\\")
    cdOrders = str(folder).split("\\")
    for order in cdOrders:
        if(str(os.getcwd()) == location):
            if order == "..":
                return "-1"
            os.chdir(order)
        else:
            os.chdir(order)
    return f"Directory change to {folder}"


appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.bind(("127.0.0.1", 2121))
appSocket.listen(1)
os.chdir("files")
location = os.getcwd()
print("\nWaiting for connecting a client...")
print("\nServer listening on 0.0.0.0:2121")

while True:
    connection, client = appSocket.accept()
    data = connection.recv(64).decode().split(" ")
    command = data[0].lower()
    print(f"Recieved: {' '.join(data)}")

    if data[0] == "!":
        break

    elif command == "help":
        connection.send(Help().encode())

    elif command == "list":
        connection.send(List().encode())

    elif command == "pwd":
        connection.send(Pwd().encode())

    elif command == "cd":
        msg = Cd(data[1], location)
        if(msg == "-1"):
            connection.send('Access denied!'.encode())
        else:
            connection.send(msg.encode())

    elif command == "dwld":
        dwoldPortNumber = random.randint(3000, 50000)
        connection.send(str(dwoldPortNumber).encode())
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.bind(('127.0.0.1', dwoldPortNumber))
        socket1.listen(5)
        while 1:
            conn, addr = socket1.accept()
            with open(data[1], 'rb') as file_to_send:
                data2 = file_to_send.read()
                conn.sendall(data2)
            conn.close()
            break
        socket1.close()
