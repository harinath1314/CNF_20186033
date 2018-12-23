
import socket

def main():
	host = socket.gethostname()
	port = 1312
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	print("server started .... !!!!")
	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode()
		print("recieving data from: "+str(addr));
		print("recieved data: "+str(data))
		data = str(data).upper()
		# print(data)
		s.sendto(data.encode(), addr)
	s.close()

if __name__ == '__main__':
	main()