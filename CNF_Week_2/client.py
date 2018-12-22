#to convert one currency to other
import socket
def client_program():
    host = "10.10.9.118"  # as both code is running on same pc
    port = 5014  # socket server port number

    c_s = socket.socket()  # instantiate
    c_s.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'end':
        c_s.send(message.encode())  # send message
        data = c_s.recv(1024).decode()  # receive response

        print('Received from server: ' + str(data))  # show in terminal

        message = input(" -> ")  # again take input

    c_s.close()  # close the connection


if __name__ == '__main__':
    client_program()
