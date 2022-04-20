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
    cdOrders = str(folder).split("\\")
    print(cdOrders)
    for order in cdOrders:
        if(str(Pwd()) == "C:\\Users\\Admin\\Desktop\\project\\server"):
            if order == "..":
                print('salam')
                return "-1"
            os.chdir(order)
        else :
            os.chdir(order)
    return f"Directory change to {folder}"


appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
appSocket.bind(("127.0.0.1", 2121))
appSocket.listen(1)



while True:
    connection, client = appSocket.accept()
    data = connection.recv(64).decode().split(" ")
    command = data[0].lower()
    print("Recieved: ", data)

    if data[0] == "!":
        break

    elif command == "help":
        connection.send(Help().encode())

    elif command == "list":
        connection.send(List().encode())

    elif command == "pwd":
        connection.send(Pwd().encode())

    elif command == "cd":
        msg = Cd(data[1])
        if(msg == "-1"):
            connection.send('Access denied!'.encode())
        else :
            connection.send(msg.encode())
    elif command == "dwld":
        dwoldPortNumber = random.randint(3000,50000)
        connection.send(str(dwoldPortNumber).encode())
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.bind(('127.0.0.1',dwoldPortNumber ))
        socket1.listen(1)
        conn, addr = socket1.accept()
        #while (1):
        reqFile = conn.recv(1024)
        with open(reqFile, 'rb') as file_to_send:
            while 1 :

                data2 = file_to_send.read(1024)
                if not data2 :
                    break
                conn.send(data2)
            file_to_send.close()
        conn.close()
