import socket

SERVER_ADDRESS = "141.226.162.89"
SERVER_PORT = 99

try:
    # create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    # send and receive messages
    message = ""
    while message != "Bye":
        message = input("Please enter your message\n")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print("The server sent: " + response)

except socket.error as e:
    print("Socket error:", e)

except KeyboardInterrupt:
    print("Keyboard interrupt, exiting...")

finally:
    # close the client socket
    client_socket.close()