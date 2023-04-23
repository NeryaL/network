import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("192.168.1.104", 8828))
my_socket.connect(("192.168.1.104", 8828))


data = ""
while data != "Bye":
    msg = input("Please enter your message\n")
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)

print("Closing client socket")
my_socket.close()