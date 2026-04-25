import socket


HOST = "localhost"
PORT = 6379


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        conn, addr = s.accept()
        with conn:
            while True:
                conn.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
