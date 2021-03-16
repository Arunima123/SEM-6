import socket
import time
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host="127.0.0.1"
port=20001
UDPServerSocket.bind((host, port))
bufferSize=1024
print("Waiting for client")
bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
address=bytesAddressPair[1]
currentTime = time.ctime(time.time())
bytesToSend=str.encode(currentTime)
UDPServerSocket.sendto(bytesToSend, address)