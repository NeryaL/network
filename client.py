import chatlib
import socket


SERVER_IP = "192.168.1.104"  # Our server will run on same computer as client
SERVER_PORT = 99

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
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((SERVER_IP, SERVER_PORT))
    return conn



def error_and_exit(error_msg):
    print(error_msg)
    exit()
    # Implement code


def login(conn):

    while True:
        username = input("Please enter username: \n")
        password = input("Please enter your password: \n")
        data = chatlib.join_data([username, password])
        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], data)

        res, _ = recv_message_and_parse(conn)
        if res == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
            print("login is ok, " + username + "! \n")
            break
        else:
            print("login failed! try again - \n")


def logout(conn):
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], '')
    res, _ = recv_message_and_parse(conn)
    if res == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
        print("you logged out successfully")
        conn.close()


def main():
    conn = connect()
    login(conn)
    logout(conn)
    pass

if __name__ == '__main__':
    main()
