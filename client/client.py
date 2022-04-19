import socket
import json
import os


def dwld(path):
    print('asd')
    receivedPort = appSocket.recv(1024).decode()
    dwldSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dwldSocket.connect(("127.0.0.1", int(receivedPort)))
    print(receivedPort)
    with open(path, 'wb') as file_to_write:
        while True:
            data = dwldSocket.recv(1024)
            if not data:
                break
            file_to_write.write(data)
        file_to_write.close()
    dwldSocket.close()


os.system("cls")
print('welcome to the FTP client:\n')
print('call one off the follwing functions:')
print('HELP              :  SHOW THIS HELP')
print('LIST              :  LIST FILES')
print('PWD               :  SHOW CURRENT DIR')
print('CD dir_name       :  CHANGE DIRECTORY')
print('DWLD file_path    :  DWNLOAD FILE')
print('QUIT              :  exit\n')
print('Enter a command: ')

while(True):

    msg = input()
    data = msg.split(' ')
    command = data[0].lower()
    try:
        if command == "clear" or command == "list" or command == "help" or command == "cd" or command == "pwd" or command == "dwld":
            appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            appSocket.connect(("127.0.0.1", 2121))
            appSocket.send(msg.encode())
            if command == 'help':
                helpServerMsg = appSocket.recv(1024).decode()
                print(helpServerMsg)
                print("\nEnter a command: ", end='')
                continue
            elif command == 'list':
                helpServerMsg = json.loads(appSocket.recv(4096).decode())
                for i in range(len(helpServerMsg)-1):
                    print(i[1] and '>' or ' ', f"\t{i[0]} - {i[2]}b")
                print(f"Total directory size: {helpServerMsg[-1]}b")
                print("\nEnter a command: ", end='')
                continue
            elif command == 'pwd':
                helpServerMsg = appSocket.recv(512).decode()
                print(helpServerMsg)
                print("\nEnter a command: ", end='')
                continue
            elif command == 'cd':
                helpServerMsg = appSocket.recv(512).decode()
                print(helpServerMsg)
                print("\nEnter a command: ", end='')
                continue
            elif command == 'clear':
                os.system("cls")
                print("\nEnter a command: ", end='')
                continue
        else:
            print("Command not found")
            print("\nEnter a command: ", end='')

    except:
        print("connection Lost!")
        break
