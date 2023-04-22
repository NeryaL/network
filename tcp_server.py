import socket
import time
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8821))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()
print("Client connected")
data = ""
NAME = "SERVER_1"
while True:
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    if data == "Quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    elif data == "NAME":
        client_socket.send(NAME.encode())
    elif data == "RAND":
        r = str(int(round(random.random()*10)))
        client_socket.send(r.encode())
    elif data == "TIME":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        client_socket.send(current_time.encode())
    client_socket.send((data.upper()+"!!!").encode())

client_socket.close()
server_socket.close()