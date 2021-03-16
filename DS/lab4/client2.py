import socket
i=0
while i<1:
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	print("Do CTRL-C to exit the program")
	msgFromClient=input("Type some text to send => ")
	print("Client sent:",msgFromClient)
	bytesToSend=str.encode(msgFromClient)
	serverAddressPort=("127.0.0.1", 20001)
	bufferSize=1024
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg1="{}".format(msgFromServer[0])
	msg="Client received: "+msg1[1:]
	print(msg)
