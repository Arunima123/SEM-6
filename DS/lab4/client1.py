import socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
bufferSize=1024
serverAddressPort=("127.0.0.1", 20001)
bytesToSend=str.encode("Send time")
UDPClientSocket.sendto(bytesToSend, serverAddressPort)	
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg1="{}".format(msgFromServer[0])
msg="Client received: "+msg1[1:]
print(msg)