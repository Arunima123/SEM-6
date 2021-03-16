import socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host="127.0.0.1"
port=20001
UDPServerSocket.bind((host, port))
bufferSize=1024

while(True):
	print("#####Server is listening#######")
	bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
	message=bytesAddressPair[0]
	address=bytesAddressPair[1]
	print(message)
	print("Do CTRL-C to exit the program")
	clientMsg1="{}".format(message)
	print("Server receievd: "+clientMsg1[1:])
	msgFromServer=input("Type some text to send => ")
	print("Sever sent: ",msgFromServer)
	bytesToSend=str.encode(msgFromServer)
	UDPServerSocket.sendto(bytesToSend, address)