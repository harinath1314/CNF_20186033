# cnf week-2 exam
# date 22-12-18
import csv
import socket

def student_attendance(data):
    print("hi i am connected")
    with open('data.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        inp = data.split(" ")
        if (inp[0] == "MARK-ATTENDANCE"):
            for row in csv_reader:
                if(inp[1]==row[0]):
                    return row[1]
            return"Attendance Not Found"
def secret_question(data):
    with open('data.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        #inp = data.split(" ")
        for row in csv_reader:
            if data == row[2]:
                return "ATTENDANCE-SUCCESS"
        return "ATTENDANCE-FAILURE"

            


def main_server():
    host = '10.10.9.118' # ip address of the host network
    port = 5014 

    s = socket.socket() # create instance of a socket
    s.bind((host,port)) # bind the socket with ip and port
    s.listen(1) # the int in argument initiates to how many clients the server can respond simultaneously
    connection, address = s.accept()
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        #data = str(conversion(str(data)))

        data = str(student_attendance(str(data)))

        print("sending:" + str(data))
        connection.send(data.encode())  # send data to the client
        while True:
            if data != "ATTENDANCE NOT FOUND":
                new_data = connection.recv(1024).decode()
            if data == "ATTENDANCE NOT FOUND":
                break
            new_data = str(secret_question(new_data))
            connection.send(new_data.encode())
            if new_data == "ATTENDANCE-SUCCESS":
            	break


        
        


    connection.close()  # close the socket connection






if __name__ == '__main__':
    main_server()