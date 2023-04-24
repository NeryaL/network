import chatlib
import socket


SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678

# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
    msg = chatlib.build_message(code, data)

    conn.send(msg.encode())
    #print("Client sent this massage: " + msg + "\n")
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

def build_send_recv_parse(conn, cmd, data):
    build_and_send_message(conn, cmd, data)
    a, b = recv_message_and_parse(conn)
    return a, b

def get_score(conn):

    back, data = build_send_recv_parse(conn, 'MY_SCORE', '')
    if back == 'YOUR_SCORE':
        print(data)
        return True
    else:
        print(data)
        return False

def get_highscore(conn):
    back, data = build_send_recv_parse(conn, 'HIGHSCORE', '')
    if back == 'ALL_SCORE':
        print(data)
        return True
    else:
        print(data)
        return False


def login(conn):

    while True:
        username = input("Please enter username: \n")
        password = input("Please enter your password: \n")
        data = chatlib.join_data([username, password])
        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], data)

        res, msg = recv_message_and_parse(conn)
        if res == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
            print("login is ok, " + username + "! \n")
            break
        else:
            print(msg)
            print("login failed! try again - \n")


def play_question(conn):

    back, data = build_send_recv_parse(conn, 'GET_QUESTION', '')

    if back == 'YOUR_QUESTION':
        data = chatlib.split_data(data, 5)
        print("question #" + data[0] + ":\n")
        for ans in data[1:]:
            print(ans)

        choise = input("choose your answer between 1-" + str(len(data)-2)+"\n")
        while int(choise) not in range(1,len(data)-2):
            choise = input("choose your answer between 1-" + str(len(data)-2)+"\n")

        answer = chatlib.join_data([data[0], choise])

        back, data = build_send_recv_parse(conn, 'SEND_ANSWER', answer)
        if back == 'CORRECT_ANSWER':
            print("correct!")
        elif back == 'WRONG_ANSWER':
            print("wrong...")
        else:
            print("some error occurred")
            return

    elif back == 'NO_QUESTIONS':
        print("no more questions...")
        return
    elif back == 'ERROR':
        print("some error occurred")
        return


def get_logged_users(conn):
    back, data = build_send_recv_parse(conn, "LOGGED", "")
    if back == 'LOGGED_ANSWER':
        print(data)
    else:
        print("some error occurred")


def logout(conn):
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], '')
    res, _ = recv_message_and_parse(conn)
    if res == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
        print("you logged out successfully")
        conn.close()


def main():
    conn = connect()
    login(conn)
    while True:
        act = input("choose action: \n1 - get your score. \n2 - get score table\n3 - log out\n"
                    + "4 - get question\n5 - get logged users\n")
        act = int(act)
        if act == 1:
            get_score(conn)
        elif act == 2:
            get_highscore(conn)
        elif act == 3:
            logout(conn)
            break
        elif act == 4:
            play_question(conn)
        elif act == 5:
            get_logged_users(conn)
        else:
            print("not an option, pls choose again\n")
    pass

if __name__ == '__main__':
    main()
