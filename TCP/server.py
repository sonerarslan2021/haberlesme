"""
https://www.youtube.com/watch?v=df0MbtvcyNs&t=331s
"""
import threading
import socket

SIZE = 50
SERVER = 'localhost'
PORT = 4444
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    connected = True
    print(f"[CONNECT] get connection {addr}")
    while connected:
        get_msg = conn.recv(SIZE).decode()
        if get_msg != '':
            print(f"[{addr}] msg : ", get_msg)
            send = 'True' + ('' * 46)
            conn.send(send.encode())

        if get_msg == "disconnect":
            connected = False

    conn.close()


def main():
    print(f"[LISTENING] server on {ADDR} listening...")
    while True:
        server.listen()
        conn, addr = server.accept()

        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()


main()
