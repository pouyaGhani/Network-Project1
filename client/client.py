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




while(True):
    os.system("cls")
    print('\n\nwelcome to the FTP client:\n\n')
    print('call one off the follwing functions:')
    print('HELP              :  SHOW THIS HELP')
    print('LIST              :  LIST FILES')
    print('PWD               :  SHOW CURRENT DIR')
    print('CD dir_name       :  CHANGE DIRECTORY')
    print('DWLD file_path    :  DWNLOAD FILE')
    print('QUIT              :  exit\n')
    print('enter a command: ')


    msg=input()
    data=msg.split(' ')
    command = data[0].lower()
    try:
        if command== "list" or command=="help" or command== "cd" or command== "pwd" or command== "dwld":
            appSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            appSocket.connect(("127.0.0.1",2121))
            appSocket.send(msg.encode())
            if command == 'help':
                os.system("cls")
                helpServerMsg = appSocket.recv(1024).decode()
                print(helpServerMsg)
                input("\nPress Enter to continue ")
                continue

    except:
        print("connection Lost!")
        break


appSocket.close()
