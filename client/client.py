import random
import socket
import json
import os

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
            # appSocket.connect(("8.tcp.ngrok.io", 15677))
            appSocket.send(msg.encode())
            if command == 'help':
                helpServerMsg = appSocket.recv(1024).decode()
                print(helpServerMsg)
                print("Enter a command: ", end='')

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

            elif command == 'dwld':
                dwldPortNumber = appSocket.recv(1024).decode()
                socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket1.connect(('127.0.0.1', int(dwldPortNumber)))
                # socket1.connect(('8.tcp.ngrok.io', 35600))
                with open(os.path.join(os.getcwd(), str(data[1])), 'wb') as file_to_write:
                    while 1:
                        data2 = socket1.recv(1024)
                        if not data2:
                            break
                        file_to_write.write(data2)
                    file_to_write.close()
                socket1.close()
                print('file downloaded successfuly!')
                print("\nEnter a command: ", end='')

        else:
            print("Command not found")
            print("\nEnter a command: ", end='')

    except:
        print("Connection lost!")
        break
