import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '172.16.58.48'
port = 12345

sock.bind((host, port))

sock.listen()

print("Hostname: ", socket.gethostbyname(host), "Port: ", port)
print("Waiting for incoming connections...\n")
conn, addr = sock.accept()

print("Received connection from ", addr[0], "(", addr[1], ")\n")
s_name = conn.recv(1024)
s_name = s_name.decode()

print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")

name = input(str("Enter your name: "))
conn.send(name.encode())

print()

while True:
	message = input(str("YOU : "))

	if message == "[e]":
		message = "Left chat room!"
		conn.send(message.encode())
		print("\n")
		sock.close()
		break

	conn.send(message.encode())
	message = conn.recv(1024)
	message = message.decode()
	print(s_name, ":", message)