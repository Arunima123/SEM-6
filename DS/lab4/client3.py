import socket

host, port = input("Enter IP and port of the server: ").split()
port = int(port) 

sock = socket.socket()
name = input(str("\nEnter your name: "))
print("\nTrying to connect to ", host, ":", port)

sock.connect((host, port))
print("Connected...\n")

sock.send(name.encode())
sock_name = sock.recv(1024)
sock_name = sock_name.decode()

print(sock_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
	message = sock.recv(1024)
	message = message.decode()
	print(sock_name, ":", message)
	message = input(str("YOU : "))
	
	if message == "[e]":
		message = "Left chat room!"
		sock.send(message.encode())
		print("\n")
		sock.close()
		break
	
	sock.send(message.encode())