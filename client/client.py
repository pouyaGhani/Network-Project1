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
print('CLEAR             :  CLEAR TERMINAL')
print('QUIT              :  EXIT\n')
print('Enter a command: ', end='')

while(True):

    msg = input()
    data = msg.split(' ')
    command = data[0].lower()
    try:
        if command == "quit" or command == "clear" or command == "list" or command == "help" or command == "cd" or command == "pwd" or command == "dwld":
            if command == 'quit':
                break

            if command == 'clear':
                os.system("cls")
                print("\nEnter a command: ", end='')
                continue

            appSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            appSocket.connect(("127.0.0.1", 2121))
            appSocket.send(msg.encode())
            if command == 'help':
                helpServerMsg = appSocket.recv(1024).decode()
                print(helpServerMsg)
                print("\nEnter a command: ", end='')

            elif command == 'list':
                helpServerMsg = json.loads(appSocket.recv(4096).decode())
                for i in range(len(helpServerMsg)-1):
                    print(
                        f"{helpServerMsg[i][1] and '>' or ' '}\t{helpServerMsg[i][0]} - {helpServerMsg[i][2]}b")
                print(f"Total directory size: {helpServerMsg[-1]}b")
                print("\nEnter a command: ", end='')

            elif command == 'pwd':
                helpServerMsg = appSocket.recv(512).decode()
                print(helpServerMsg)
                print("\nEnter a command: ", end='')

            elif command == 'cd':
                helpServerMsg = appSocket.recv(512).decode()
                print(helpServerMsg)
                print("\nEnter a command: ", end='')

        else:
            print("Command not found")
            print("\nEnter a command: ", end='')

    except:
        print("connection Lost!")
        break
