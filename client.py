import chatlib  # To use chatlib functions or consts, use chatlib.****
import socket

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678

# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
    msg = chatlib.build_message(code, data)

    conn.send(msg.encode())
    print("Client sent this massage: " + msg + "\n")
    return 
	

def recv_message_and_parse(conn):
    """
    Recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message.
    If error occured, will return None, None
    """
    resp = conn.recv(1024).decode()
    cmd, data = chatlib.parse_message(resp)
    return cmd, data

	
	

def connect():
    # Implement Code
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    socket.connect((SERVER_IP, SERVER_PORT))

    return socket


def error_and_exit(error_msg):
    print(error_msg)
    exit()
    # Implement code


def login(conn):
    username = input("Please enter username: \n")
    # Implement code
	
	build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"],"")
	
	# Implement code
	
    pass

def logout(conn):
    # Implement code
    pass

def main():
    # Implement code
    pass

if __name__ == '__main__':
    main()
